from flask import Blueprint, request, jsonify, send_file
from app.s3_utils import upload_file_to_s3, download_file_from_s3, list_files_in_s3
import os

api = Blueprint('api', __name__)

@api.route('/upload', methods=['POST'])
def upload():
    """
    Upload a file to AWS S3.
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file part in request"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No file selected for upload"}), 400

    try:
        upload_file_to_s3(file)
        return jsonify({"message": f"File '{file.filename}' uploaded successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api.route('/download/<filename>', methods=['GET'])
def download(filename):
    """
    Download a file from AWS S3.
    """
    try:
        local_path = download_file_from_s3(filename)
        return send_file(local_path, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api.route('/list', methods=['GET'])
def list_files():
    """
    List all files stored in AWS S3.
    """
    try:
        files = list_files_in_s3()
        return jsonify({"files": files}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api.route('/', methods=['GET'])
def index():
    """
    Health check endpoint.
    """
    return jsonify({"message": "File Storage Microservice is running!"}), 200