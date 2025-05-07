from database import get_conn, put_conn
import json

def callDatabase(selectView):
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            #cur.execute("SELECT public.getall();")
            query = f"SELECT jsonb_agg(p) FROM {selectView} p"
            cur.execute(query)
            result = cur.fetchone()[0]
            print(result)
            return result
    finally:
        put_conn(conn)


def getReviewProfessors(target):
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT to_jsonb(p.*) FROM reviews p WHERE target_type = 'professor' AND target_id = %s;", (target,))
            tmp = cur.fetchall()
            # print(f'getAll : {tmp}')
            result = [row[0] for row in tmp]
            total = sum(r['rating'] for r in result)
            avg = total / len(result) if result else 0

            cur.execute("SELECT to_jsonb(p.*) FROM professors p WHERE id = %s;", (target,))
            professor_info = cur.fetchone()
            professor = professor_info[0] if professor_info else {}

            # print(f'getReview: {result}')
            return result, avg, professor
    finally:
        put_conn(conn)

