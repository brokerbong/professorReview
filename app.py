from flask import Flask, render_template, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)

PROFESSORS = [
    {"id": 1, "name": "홍길동", "department": "컴퓨터공학과", "email": 'jeonsoegbong1@gmail.com', "phone":"phone1"},
    {"id": 2, "name": "김유신", "department": "전자공학과", "email": 'jeonsoegbong2@gmail.com', "phone":"phone2"}
]

LECTURES = [
    {"id": 1, "title": "자료구조", "professor_name": "홍길동"},
    {"id": 2, "title": "회로이론", "professor_name": "김유신"}
]

REVIEWS = {
    "professor": {
        1: [{"writer": "학생1", "password": generate_password_hash("p1"), "rating": 5,
             "comment": "정말 훌륭해요", "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")}],
        2: []
    },
    "lecture": {
        1: [{"writer": "학생2", "password": generate_password_hash("p2"), "rating": 4,
             "comment": "유익한 수업입니다", "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")}],
        2: []
    }
}

@app.route('/')
def index():
    #request.args.get('key', '기본값') view에 값이없으면 professor 자동 bind
    view = request.args.get('view', 'professor')

    
    selected_id = request.args.get('professor_id' if view == 'professor' else 'lecture_id', type=int)
    print(f'request args: {request.args}, view :{view}')
    
    target_list = PROFESSORS if view == 'professor' else LECTURES
    target = next((x for x in target_list if x["id"] == selected_id), None)


    reviews = REVIEWS[view].get(selected_id, []) if target else []
    avg_rating = round(sum(r["rating"] for r in reviews) / len(reviews), 1) if reviews else None

    return render_template(
        "base.html",
        view=view, # view is url
        professors=PROFESSORS,
        lectures=LECTURES,
        professor=target if view == 'professor' else None,
        lecture=target if view == 'lecture' else None,
        reviews=reviews,
        avg_rating=avg_rating
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
