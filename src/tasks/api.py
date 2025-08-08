from openai import OpenAI
from src.models.prompt_model import UserPrompt, ChatResponse
from src.config import API_KEY
from src.workers.celery_app import celery

client = OpenAI(api_key=API_KEY, base_url="https://api.deepseek.com")

@celery.task
def ask_api(user: dict) -> dict:
    user_prompt = user["user_prompt"]

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": user_prompt},
        ],
        stream=False
    )

    return {
            "user_prompt": user_prompt,
            "output": response.choices[0].message.content
            }

