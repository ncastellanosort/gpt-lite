from fastapi import FastAPI
from src.routes.prompt_router import prompt_rt
import src.config

app = FastAPI()

app.include_router(prompt_rt)
