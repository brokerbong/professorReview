from psycopg2 import pool
from psycopg2.pool import SimpleConnectionPool
import os

# 환경 변수 또는 하드코딩 가능 (보안상 환경 변수 권장)
DB_HOST = "c5hilnj7pn10vb.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com"
DB_PORT = 5432
DB_NAME = "d2m7pqo5ucoj9p"
DB_USER = "ubhn5jf7o0a2rl"
DB_PASSWORD = "p7f603737160f86855834796b40c3a7c1c47e04712922052ae002d47ea8c95df1"

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