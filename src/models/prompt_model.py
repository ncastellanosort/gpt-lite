from pydantic import BaseModel
from typing import Optional

class UserPrompt(BaseModel):
    user_prompt: str

class ChatResponse(BaseModel):
    user_prompt: str
    output: Optional[str] = None
