from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from src.models.prompt_model import UserPrompt
from src.tasks.api import ask_api

prompt_rt = APIRouter()

@prompt_rt.post("/ask")
def home(user_prompt: UserPrompt):
    res = ask_api.delay(user_prompt.dict())
    # return JSONResponse(content=jsonable_encoder(res), status_code=status.HTTP_200_OK)
    return JSONResponse(content={"message": "celery esta con la respuesta"}, status_code=status.HTTP_200_OK)
