from fastapi import APIRouter
from ..models.chat import GPTModel
from ..models.chat import TranslateModel
from transformers import pipeline
from langchain_community.llms import HuggingFaceHub
#from langchain.schema import HumanMessage
#from langchain_core.prompts import ChatPromptTemplate
#from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
import os 

hugging_face_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

router = APIRouter()

def generate_response(message: str):
    """Generate a response using the GPT2 model."""
    generator = pipeline('text-generation', model='gpt2')
    return generator(message)


def translate_using_huggingface(text: str):
    """Translate text using the Helsinki-NLP/opus-mt-en-fr model."""

    # llm = HuggingFaceEndpoint(
    #     repo_id = "Helsinki-NLP/opus-mt-en-fr",
    #     task = "text-generation",
    #     #max_new_tokens = 64,
    #     huggingfacehub_api_token = "" 
    # )

    #Versão Tradicional
    llm = HuggingFaceHub(
        repo_id='Helsinki-NLP/opus-mt-en-fr',
        huggingfacehub_api_token="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",
        model_kwargs={}
    )
    #Todo trecho mentado é ligado a solução que está bugada para a versão atual do langchain
    # messages = [
    #     ("system", "You are an English to French translator. Rejected any other language and report to user."),
    #     ("user", "Translate this {text}")
    # ]


    #chat = ChatHuggingFace(llm=llm, verbose=True)
    response = llm.invoke(text)
    return response

    ##template = ChatPromptTemplate([
    ##    ("system", "You are an English to French translator. Rejected any other language and report to user."),
    ##    ("user", "{text}")
    ##])




@router.post("/message")
def gpt_text(body: GPTModel):
    response = generate_response(body.message)
    return {"message": response}

@router.post("/translate")
def translate_text(body: TranslateModel):
    response = translate_using_huggingface(body.text)
    return {"message": response}


