import psycopg2
from src.config import POSTGRES_URL

conn = psycopg2.connect(POSTGRES_URL)


