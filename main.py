from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {
        "greeting": "Assalamu Alaikum",
        "message": "Oh You Find me!! Thank you for come here. This is a simple example Not a big Deal",
        "autor": "- Nurullah Sadekeen"}