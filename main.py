from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {
        "greeting": "Oh You Find me!!",
        "message": "Thank you  for come here. This is a simple example Not a big Deal",
        "autor": "- Nurullah Sadekeen"}