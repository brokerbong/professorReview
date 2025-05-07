from database import get_conn, put_conn
import json

def callDatabase(selectView):
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT public.getall();")
            result = cur.fetchone()[0]


            if (selectView == "professor"):
                return result
            if (selectView == "lecture"):
                return result
    finally:
        put_conn(conn)


def getReview(target):
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT to_jsonb(p.*) FROM reviews p;")
            result = [row[0] for row in cur.fetchall()]
            # result = json.loads(cur.fetchone()[0])
            print(f'getReview: {result}')
            
            return result
    finally:
        put_conn(conn)