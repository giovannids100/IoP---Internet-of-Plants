from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()
value = {}

@app.post("/api/dati")
async def ricevi_dati(request: Request):
    global value
    body = await request.json()
    value = body
    return {"status": "ok"}

@app.get("/api/value")
def leggi_ultimo():
    return value

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)