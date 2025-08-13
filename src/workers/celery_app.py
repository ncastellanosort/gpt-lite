from celery import Celery
from src.config import REDIS_URL

celery = Celery("worker", broker=REDIS_URL)

celery.autodiscover_tasks(["src.tasks"])
from src.tasks import prompt_tasks

