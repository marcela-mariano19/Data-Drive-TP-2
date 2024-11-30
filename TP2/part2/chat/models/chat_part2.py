from pydantic import BaseModel

class ChatModel(BaseModel):
    message: str

class TranslateModel(BaseModel):
    text: str