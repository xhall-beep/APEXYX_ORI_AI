import asyncio
import os
from fastapi import FastAPI
from fastapi.websockets import WebSocket
import uvicorn

app = FastAPI()

@app.websocket("/terminal")
async def terminal_websocket(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            cmd = data.get("command")
            proc = await asyncio.create_subprocess_shell(
                cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                cwd=os.path.expanduser("~")
            )
            stdout, stderr = await proc.communicate()
            output = (stdout.decode() + stderr.decode()).strip()
            # Escaping for JSON safety
            safe_output = output.replace('"', '\\"').replace('\n', '<br>')
            await websocket.send_json({"output": safe_output})
    except Exception as e:
        print(f"WS Error: {e}")

@app.get("/")
async def health():
    return {"status": "SOVEREIGN_REECH_ONLINE", "port": 58081}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=58081)
