import asyncio
from fastapi import FastAPI, Request
import uvicorn
import os

app = FastAPI()

@app.post("/command")
async def execute_command(request: Request):
    data = await request.json()
    cmd = data.get("command")
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        cwd=os.path.expanduser("~")
    )
    stdout, stderr = await proc.communicate()
    return {
        "status": "complete",
        "returncode": proc.returncode,
        "stdout": stdout.decode().strip(),
        "stderr": stderr.decode().strip()
    }

@app.get("/")
async def health():
    return {"status": "SOVEREIGN_RECH_ONLINE", "ip": "10.0.0.203"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=58080)
