from openai import OpenAI
from src.models.prompt_model import UserPrompt, ChatResponse
from src.config import API_KEY

client = OpenAI(api_key=API_KEY, base_url="https://api.deepseek.com")

def ask_api(user: UserPrompt) -> ChatResponse:
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": user.user_prompt},
        ],
        stream=False
    )

    return ChatResponse(
            user_prompt=user.user_prompt,
            output=response.choices[0].message.content
            )

