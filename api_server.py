from fastapi import FastAPI, Request
from db import log_ip
import uvicorn

app = FastAPI()

@app.post("/update-ip")
async def update_ip(request: Request):
    data = await request.json()
    local_ip = data.get("local_ip")
    public_ip = data.get("public_ip")

    if not local_ip or not public_ip:
        return {"error": "Missing IP values"}

    log_ip(local_ip, public_ip)
    return {"status": "success"}

if __name__ == "__main__":
    uvicorn.run("api_server:app", host="0.0.0.0", port=8000)
