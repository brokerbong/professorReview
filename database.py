from psycopg2 import pool
from psycopg2.pool import SimpleConnectionPool
import os

# 환경 변수 또는 하드코딩 가능 (보안상 환경 변수 권장)
DB_HOST = ""
DB_PORT = 5432
DB_NAME = ""
DB_USER = ""
DB_PASSWORD = ""

# 커넥션 풀 생성
db_pool = SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

def get_conn():
    return db_pool.getconn()

def put_conn(conn):
    db_pool.putconn(conn)

def close_all():
    db_pool.closeall()
