from pydantic import BaseModel

class GPTModel(BaseModel):
    message: str

class TranslateModel(BaseModel):
    text: str