from fastapi import FastAPI
from .routes.chat import router as chat_router
import os


app = FastAPI()


app.include_router(chat_router)

@app.get("/")
async def root():
    return {f"message": "API is running"}