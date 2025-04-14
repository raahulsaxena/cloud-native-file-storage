from flask import Blueprint, request, jsonify, send_file
from app.s3_utils import upload_file_to_s3, download_file_from_s3, list_files_in_s3

api = Blueprint('api', __name__)

@api.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        upload_file_to_s3(file)
        return jsonify({"message": "Upload successful"}), 200
    return jsonify({"error": "No file provided"}), 400

@api.route('/download/<filename>', methods=['GET'])
def download(filename):
    path = download_file_from_s3(filename)
    return send_file(path, as_attachment=True)

@api.route('/list', methods=['GET'])
def list_files():
    files = list_files_in_s3()
    return jsonify({"files": files})