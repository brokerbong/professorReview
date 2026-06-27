from psycopg2 import pool
from psycopg2.pool import SimpleConnectionPool
import os

DB_HOST     = os.getenv("DB_HOST")
DB_PORT     = os.getenv("DB_PORT")
DB_NAME     = os.getenv("DB_NAME")
DB_USER     = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

db_pool = None

def get_pool():
    global db_pool
    if db_pool is None:
        db_pool = SimpleConnectionPool(
            minconn=1, maxconn=10,
            host=DB_HOST, port=DB_PORT,
            database=DB_NAME, user=DB_USER, password=DB_PASSWORD
        )
    return db_pool

def get_conn():
    return get_pool().getconn()

def put_conn(conn):
    get_pool().putconn(conn)

def close_all():
    if db_pool:
        db_pool.closeall()
