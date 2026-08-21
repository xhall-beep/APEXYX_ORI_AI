"""APEXYX Mesh Console — self-contained Android app (Kivy).

The app's job: a pocket mesh node. It runs a tamper-evident, append-only
task/event bus in the app's own storage — the same sealed hash-chain model as
the APEXYX Mesh core — with a live console UI:

  * POST a task onto the bus
  * CLAIM the oldest open task
  * COMPLETE the claimed task
  * VERIFY the full seal chain (detects any tampering with history)

Dependencies: python3 + kivy + stdlib sqlite3/hashlib ONLY, so python-for-android
can bundle every import into the APK. The desktop/server stack in this repo
(server_main.py, frida/androguard tooling) intentionally stays host-side.
"""

import hashlib
import json
import os
import sqlite3
import time

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

GENESIS = "APEXYX-GENESIS"

BG = (0.04, 0.05, 0.08, 1)
PANEL = (0.09, 0.11, 0.16, 1)
ACCENT = (0.13, 0.77, 0.37, 1)
ACCENT_DIM = (0.10, 0.45, 0.25, 1)
DANGER = (0.85, 0.25, 0.25, 1)
TEXT = (0.88, 0.92, 0.95, 1)


class MeshBus:
    """Append-only sqlite event bus with a sha256 seal chain."""

    def __init__(self, db_path):
        self.db_path = db_path
        con = self._con()
        con.execute(
            "CREATE TABLE IF NOT EXISTS events ("
            " id INTEGER PRIMARY KEY AUTOINCREMENT,"
            " ts REAL NOT NULL,"
            " kind TEXT NOT NULL,"
            " payload TEXT NOT NULL,"
            " seal TEXT NOT NULL)"
        )
        con.commit()
        con.close()

    def _con(self):
        con = sqlite3.connect(self.db_path, timeout=10)
        con.execute("PRAGMA journal_mode=WAL")
        return con

    @staticmethod
    def _seal(prev_seal, ts, kind, payload):
        material = "|".join((prev_seal, repr(ts), kind, payload))
        return hashlib.sha256(material.encode("utf-8")).hexdigest()

    def append(self, kind, payload_dict):
        con = self._con()
        try:
            row = con.execute(
                "SELECT seal FROM events ORDER BY id DESC LIMIT 1"
            ).fetchone()
            prev = row[0] if row else GENESIS
            ts = time.time()
            payload = json.dumps(payload_dict, sort_keys=True)
            seal = self._seal(prev, ts, kind, payload)
            con.execute(
                "INSERT INTO events (ts, kind, payload, seal) VALUES (?,?,?,?)",
                (ts, kind, payload, seal),
            )
            con.commit()
            return seal
        finally:
            con.close()

    def events(self, limit=200):
        con = self._con()
        try:
            rows = con.execute(
                "SELECT id, ts, kind, payload, seal FROM events"
                " ORDER BY id DESC LIMIT ?",
                (limit,),
            ).fetchall()
            return rows
        finally:
            con.close()

    def verify_chain(self):
        """Recompute every seal. Returns (ok, checked, first_bad_id)."""
        con = self._con()
        try:
            rows = con.execute(
                "SELECT id, ts, kind, payload, seal FROM events ORDER BY id ASC"
            ).fetchall()
        finally:
            con.close()
        prev = GENESIS
        for rid, ts, kind, payload, seal in rows:
            expect = self._seal(prev, ts, kind, payload)
            if expect != seal:
                return False, len(rows), rid
            prev = seal
        return True, len(rows), None

    # -- task views over the event log ------------------------------------
    def _task_states(self):
        states = {}
        for _id, _ts, kind, payload, _seal in reversed(self.events(limit=1000)):
            p = json.loads(payload)
            tid = p.get("task_id")
            if kind == "task.post":
                states[tid] = ("open", p.get("text", ""))
            elif kind == "task.claim" and tid in states:
                states[tid] = ("claimed", states[tid][1])
            elif kind == "task.done" and tid in states:
                states[tid] = ("done", states[tid][1])
        return states

    def post_task(self, text):
        tid = hashlib.sha256(f"{time.time()}|{text}".encode()).hexdigest()[:12]
        self.append("task.post", {"task_id": tid, "text": text})
        return tid

    def claim_oldest_open(self):
        for tid, (state, text) in self._task_states().items():
            if state == "open":
                self.append("task.claim", {"task_id": tid})
                return tid, text
        return None, None

    def complete_claimed(self):
        for tid, (state, text) in self._task_states().items():
            if state == "claimed":
                self.append("task.done", {"task_id": tid})
                return tid, text
        return None, None

    def counts(self):
        c = {"open": 0, "claimed": 0, "done": 0}
        for state, _ in self._task_states().values():
            c[state] = c.get(state, 0) + 1
        return c


class ConsoleUI(BoxLayout):
    def __init__(self, bus, **kw):
        super().__init__(orientation="vertical", padding=12, spacing=8, **kw)
        self.bus = bus

        self.status = Label(
            text="APEXYX MESH CONSOLE", bold=True, color=ACCENT,
            size_hint_y=None, height=34, font_size="18sp",
        )
        self.add_widget(self.status)

        self.counts_lbl = Label(
            text="", color=TEXT, size_hint_y=None, height=24, font_size="13sp"
        )
        self.add_widget(self.counts_lbl)

        entry_row = BoxLayout(size_hint_y=None, height=48, spacing=8)
        self.entry = TextInput(
            hint_text="task text...", multiline=False,
            background_color=PANEL, foreground_color=TEXT,
            cursor_color=ACCENT, padding=(10, 12),
        )
        post_btn = Button(
            text="POST", size_hint_x=None, width=90,
            background_normal="", background_color=ACCENT_DIM, color=TEXT,
        )
        post_btn.bind(on_release=self.on_post)
        self.entry.bind(on_text_validate=self.on_post)
        entry_row.add_widget(self.entry)
        entry_row.add_widget(post_btn)
        self.add_widget(entry_row)

        btn_row = BoxLayout(size_hint_y=None, height=44, spacing=8)
        for label, cb in (
            ("CLAIM", self.on_claim),
            ("COMPLETE", self.on_complete),
            ("VERIFY CHAIN", self.on_verify),
        ):
            b = Button(
                text=label, background_normal="",
                background_color=PANEL, color=ACCENT, font_size="13sp",
            )
            b.bind(on_release=cb)
            btn_row.add_widget(b)
        self.add_widget(btn_row)

        scroll = ScrollView()
        self.log_lbl = Label(
            text="", color=TEXT, font_size="12sp", halign="left",
            valign="top", size_hint_y=None, markup=True,
        )
        self.log_lbl.bind(
            width=lambda i, w: setattr(i, "text_size", (w - 8, None)),
            texture_size=lambda i, ts: setattr(i, "height", ts[1] + 12),
        )
        scroll.add_widget(self.log_lbl)
        self.add_widget(scroll)

        self.refresh()
        Clock.schedule_interval(lambda dt: self.refresh(), 3)

    # -- actions -----------------------------------------------------------
    def on_post(self, *_):
        text = self.entry.text.strip()
        if not text:
            self.flash("empty task ignored", DANGER)
            return
        tid = self.bus.post_task(text)
        self.entry.text = ""
        self.flash(f"posted {tid}", ACCENT)
        self.refresh()

    def on_claim(self, *_):
        tid, text = self.bus.claim_oldest_open()
        if tid:
            self.flash(f"claimed {tid}: {text[:40]}", ACCENT)
        else:
            self.flash("no open tasks", DANGER)
        self.refresh()

    def on_complete(self, *_):
        tid, text = self.bus.complete_claimed()
        if tid:
            self.flash(f"done {tid}: {text[:40]}", ACCENT)
        else:
            self.flash("no claimed tasks", DANGER)
        self.refresh()

    def on_verify(self, *_):
        ok, checked, bad = self.bus.verify_chain()
        if ok:
            self.flash(f"seal chain OK — {checked} events verified", ACCENT)
        else:
            self.flash(f"CHAIN BROKEN at event #{bad}", DANGER)
        self.refresh()

    # -- rendering ----------------------------------------------------------
    def flash(self, msg, color):
        self.status.text = msg
        self.status.color = color

    def refresh(self):
        c = self.bus.counts()
        self.counts_lbl.text = (
            f"open {c['open']}   claimed {c['claimed']}   done {c['done']}"
        )
        lines = []
        for rid, ts, kind, payload, seal in self.bus.events(limit=80):
            t = time.strftime("%H:%M:%S", time.localtime(ts))
            p = json.loads(payload)
            desc = p.get("text") or p.get("task_id", "")
            lines.append(
                f"[color=2bc55e]#{rid} {t}[/color] "
                f"[b]{kind}[/b] {desc}  [color=555f6e]{seal[:10]}[/color]"
            )
        self.log_lbl.text = "\n".join(lines) if lines else "bus empty — post a task"


class ApexyxOriApp(App):
    title = "APEXYX Mesh Console"

    def build(self):
        Window.clearcolor = BG
        db = os.path.join(self.user_data_dir, "mesh_bus.db")
        bus = MeshBus(db)
        if not bus.events(limit=1):
            bus.append("node.boot", {"node": "apexyx-ori", "v": "1.0.0"})
        return ConsoleUI(bus)


if __name__ == "__main__":
    ApexyxOriApp().run()
