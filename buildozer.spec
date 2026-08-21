[app]
title = APEXYX_ORI_AI
package.name = apexyxori
package.domain = org.apexyx
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt
version = 1.0.0

# NOTE: main.py (APEXYX Mesh Console) is fully self-contained: kivy + stdlib
# sqlite3/hashlib only, all bundleable by python-for-android. Keeping this list
# minimal maximizes build success. The desktop/server stack in this repo
# (server_main.py, frida, androguard, adbutils, fastapi, uvicorn, mcp,
# pydantic_ai, GitPython) has NO p4a recipe and intentionally stays host-side.
requirements = python3,kivy

orientation = portrait
fullscreen = 0

# Target Android configuration
android.api = 33
android.minapi = 30
android.ndk = 25b
android.ndk_api = 30
android.archs = arm64-v8a
android.accept_sdk_license = True
android.allow_backup = True

# Downgrade the hostpython3 sem_clockwait halt from error to warning. bionic
# resolves the symbol at runtime on API >= 30, so the compile can proceed.
# (The real fix is -Wno-error; -DHAVE_SEM_CLOCKWAIT=0 is unreliable because
# pyconfig.h re-#defines it to 1, so it is intentionally omitted here.)
android.p4a_extra_args = --extra-cflags="-Wno-error=implicit-function-declaration"

[buildozer]
log_level = 2
warn_on_root = 1
