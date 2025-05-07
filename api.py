from flask import Blueprint, jsonify, request, render_template
from datetime import datetime

from function import getReview

api = Blueprint('api', __name__)


# 교수 상세 정보 API
@api.route('/api/professor/<int:professor_id>')
def api_professor(professor_id):
    print(f"professor{professor_id}")

    writer = 'AAAA'
    password = 'asdf'
    rating = 4
    comment = 'aaa'
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # reviews = [{
    #     "writer" : writer,
    #     "password": password,
    #     "rating": rating,
    #     "comment": comment,
    #     "created_at": created_at
    # }]

    reviews = getReview(professor_id)
    print(reviews)
    avg_rating = 4.5
    infoData = {
        'id' : '1',
        'name' : 'test'+str(professor_id),
        'professor' : 'tttt'
    }
    return render_template("components/review_panel.html", type="professor", reviews=reviews, avg_rating=avg_rating, infoData=infoData)


# 강의 상세 정보 API
@api.route('/api/lecture/<int:lecture_id>')
def api_lecture(lecture_id):
    print(f"lecture {lecture_id}")
    return str(lecture_id)

## 자료 상세 정보 API
@api.route('/api/resource/<int:resource_id>')
def api_resource(resource_id):
    print(f"lecture{resource_id}")
    return str(resource_id)