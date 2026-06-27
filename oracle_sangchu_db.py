import os
import oracledb
from dotenv import load_dotenv

load_dotenv()

ORACLE_USER = os.getenv("ORACLE_USER")
ORACLE_PASSWORD = os.getenv("ORACLE_PASSWORD")
ORACLE_DSN = os.getenv("ORACLE_DSN")

oracle_pool = None


def get_oracle_pool():
    global oracle_pool

    if oracle_pool is None:
        oracle_pool = oracledb.create_pool(
            user=ORACLE_USER,
            password=ORACLE_PASSWORD,
            dsn=ORACLE_DSN,
            min=1,
            max=5,
            increment=1
        )

    return oracle_pool


def get_sangchu_conn():
    return get_oracle_pool().acquire()


def test_connection():
    with get_sangchu_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM DUAL")
            return cursor.fetchone()
