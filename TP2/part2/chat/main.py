from fastapi import FastAPI
from .routes.chat_part2 import router as chat_router
import os


app = FastAPI()


app.include_router(chat_router, prefix="/part2")

@app.get("/")
async def root():
    return {f"message": "API is running - Part 2"}