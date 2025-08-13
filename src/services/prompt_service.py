from src.config import POSTGRES_URL
import psycopg2

def store_prompt(response: dict):
    try:
        with psycopg2.connect(POSTGRES_URL) as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO prompts (user_prompt, chat_response) VALUES (%s, %s)",
                    (response["user_prompt"], response["output"])
                )
                conn.commit()
    except Exception as e:
        print(f"err saving prompt {e}")
