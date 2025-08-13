from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from src.models.prompt_model import UserPrompt
from src.api_services.api import ask_api

prompt_rt = APIRouter()

@prompt_rt.post("/ask")
def home(user_prompt: UserPrompt):
    res = ask_api(user_prompt)
    return JSONResponse(content=jsonable_encoder(res), status_code=status.HTTP_200_OK)
