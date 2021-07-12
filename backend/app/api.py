from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = [
    "http://localhost:3000",
    "localhost:3000"
]


@app.get("/api", tags=["root"])
async def read_root():
    return {"message": "Welcome to your todo list"}
