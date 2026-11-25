import os

import psycopg
from dotenv import load_dotenv
from psycopg.rows import dict_row


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise RuntimeError("Falta DATABASE_URL en el archivo .env")


def conectar():
    return psycopg.connect(
        DATABASE_URL,
        row_factory=dict_row
    )
