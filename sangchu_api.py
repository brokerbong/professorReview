from flask import Blueprint, request, jsonify
from oracle_sangchu_db import get_sangchu_conn

sangchu = Blueprint('sangchu', __name__)

@sangchu.route('/upload-image', methods=['POST'])
def upload_image():
    image_data = request.data
    if not image_data:
        return jsonify({'error': 'no image'}), 400

    with get_sangchu_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO sangchu_images (image_data) VALUES (:1)",
                (image_data,)
            )
            conn.commit()

    print(f"[sangchu] 이미지 저장 완료: {len(image_data)} bytes")
    return jsonify({'status': 'ok'}), 200


@sangchu.route('/upload-sensor', methods=['POST'])
def upload_sensor():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'no data'}), 400

    soil_raw      = data.get('soil_raw')
    soil_percent  = data.get('soil_percent')
    light_raw     = data.get('light_raw')
    light_percent = data.get('light_percent')

    with get_sangchu_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO sangchu_sensors (soil_raw, soil_percent, light_raw, light_percent) VALUES (:1, :2, :3, :4)",
                (soil_raw, soil_percent, light_raw, light_percent)
            )
            conn.commit()

    print(f"[sangchu] 센서 저장: soil={soil_raw}({soil_percent}%), light={light_raw}({light_percent}%)")
    return jsonify({'status': 'ok'}), 200
