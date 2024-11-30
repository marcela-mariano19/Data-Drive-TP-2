from fastapi import APIRouter
from ..models.chat_part2 import ChatModel
from ..models.chat_part2 import TranslateModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

import os 


from transformers import pipeline
from langchain_community.llms import FakeListLLM, HuggingFaceHub
#from langchain.schema import HumanMessage
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace


hugging_face_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

router = APIRouter()

def generate_response_fake(message: str):
    """Generate a response using a fake LLM."""
    llm = FakeListLLM(response="É importante usar a biblioteca Fake List LLM para gerar respostas, pois ea evita que os recursos sejam gastos de maneira desnecessária.")	
    response = llm.invoke(message)
    return response

os.environ["GOOGLE_API_KEY"] = "AIzaSyDt3ne03smUB19zpO-EaHE-ESWd-XsIj9Y"

def generate_translation_gemini(text: str):
    """Generate a translation using Gemini. Translate from English to French."""
    template = ChatPromptTemplate(
        [("system", "You are an English to French translator."),
         ("user", "Translate trhis: {text}")
        
        ])
    
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
    response = llm.invoke(template.format_messages(text=text))

    return response.content


def generate_translation_huggingface_german(text: str):
    """Generate a translation using the Helsinki-NLP/opus-mt-en-de model. Translate from English to German."""
    llm = HuggingFaceHub(
        repo_id='Helsinki-NLP/opus-mt-en-de',
        huggingfacehub_api_token="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",
        model_kwargs={}
    )
    response = llm.invoke(text)
    return response

@router.post("/fake")
def translate_text(body: ChatModel):
    response = generate_response_fake(body.text)
    return {"message": response}

@router.post("/translate")
def translate_text(body: TranslateModel):
    response = generate_translation_gemini(body.text)
    return {"message": response}

@router.post("/translate_german")
def translate_text(body: TranslateModel):
    response = generate_translation_huggingface_german(body.text)
    return {"message": response}





