from fastapi import FASTAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}