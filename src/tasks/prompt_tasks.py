from src.workers.celery_app import celery
from src.services.prompt_service import store_prompt

@celery.task
def store_prompt_task(response: dict):
    store_prompt(response)
