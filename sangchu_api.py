import boto3
import os
from flask import Blueprint, request, jsonify
from datetime import datetime

sangchu = Blueprint('sangchu', __name__)

s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION', 'ap-northeast-2')
)
BUCKET = os.getenv('AWS_S3_BUCKET')

@sangchu.route('/upload-image', methods=['POST'])
def upload_image():
    image_data = request.data
    if not image_data:
        return jsonify({'error': 'no image'}), 400

    filename = f"sangchu/{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.jpg"
    s3.put_object(Bucket=BUCKET, Key=filename, Body=image_data, ContentType='image/jpeg')
    image_url = f"https://{BUCKET}.s3.amazonaws.com/{filename}"

    print(f"[sangchu] 이미지 저장: {image_url}")
    # TODO: DB 저장 (테이블 준비 후)

    return jsonify({'url': image_url}), 200


@sangchu.route('/upload-sensor', methods=['POST'])
def upload_sensor():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'no data'}), 400

    print(f"[sangchu] 센서: soil={data.get('soil_raw')}({data.get('soil_percent')}%), "
          f"light={data.get('light_raw')}({data.get('light_percent')}%)")
    # TODO: DB 저장 (테이블 준비 후)

    return jsonify({'status': 'ok'}), 200
