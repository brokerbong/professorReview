from flask import Blueprint, jsonify, request, render_template
from datetime import datetime

from function import getReviewProfessors

api = Blueprint('api', __name__)


# 교수 상세 정보 API
@api.route('/api/professors/<int:professor_id>')
def api_professor(professor_id):
    print(f"professor{professor_id}")

    reviews, avg_score, infoData = getReviewProfessors(professor_id)
    # print(reviews)

    return render_template("components/review_panel.html", 
                            type="professors", 
                            reviews=reviews, 
                            avg_rating=avg_score, 
                            infoData=infoData)


# 강의 상세 정보 API
@api.route('/api/lectures/<int:lecture_id>')
def api_lecture(lecture_id):
    print(f"lecture {lecture_id}")
    return str(lecture_id)


## 자료 상세 정보 API
@api.route('/api/resource/<int:resource_id>')
def api_resource(resource_id):
    print(f"lecture{resource_id}")
    return str(resource_id)