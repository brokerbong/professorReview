from flask import Flask, render_template, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash


from api import api

from database import get_conn, put_conn
from function import callDatabase

app = Flask(__name__)
app.register_blueprint(api)  # 등록

@app.route("/test-db")
def test_db():
    conn = get_conn()
    name = 'Test'
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT public.createtest(%s);", (name,))
            result = cur.fetchone()[0]
            conn.commit()
            return f"DB 연결 성공: {result}"
    finally:
        put_conn(conn)

@app.route('/')
def index():
    #request.args.get('key', '기본값') view에 값이없으면 professor 자동 bind
    view = request.args.get('view', 'professor')
    profileData = callDatabase(view)
    print(f'data: {profileData}')
    return render_template(
        "base.html",
        view=view, # view is url
        datas=profileData
    )

@app.route('/review/<string:view>/<int:item_id>', methods=['POST'])
def submit_review(view, item_id):
    writer = request.form['writer']
    password = generate_password_hash(request.form['password'])
    rating = int(request.form['rating'])
    comment = request.form['comment']
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    review = {
        "writer": writer,
        "password": password,
        "rating": rating,
        "comment": comment,
        "created_at": created_at
    }

    REVIEWS[view].setdefault(item_id, []).append(review)
    return redirect(f"/?view={view}&{'professor_id' if view == 'professor' else 'lecture_id'}={item_id}")



if __name__ == '__main__':
    app.run(debug=True)



