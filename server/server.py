from logging import info
from flask_cors import CORS
from http import HTTPStatus
from os import makedirs, unlink
from os.path import exists, join
from server.transpile import Transpiler
from server.config import Config, ALLOWED_EXTENSIONS
from flask import Flask, jsonify, request, send_from_directory


def create_app(config_class=Config) -> Flask:
    api: Flask = Flask(__name__)
    api.config.from_object(Config)
    
    # Allow all orgins to access all routes
    CORS(api)
    
    # Helper function to check if the file has a valid extension
    def allowed_file(filename):
        return "." in filename and filename.split(".")[-1].lower() in ALLOWED_EXTENSIONS
    
    # Helper function to remove .zip files after uploading to the client
    def unzip(filepath):
        info("ℹ️ Processing .zip cleanup! ℹ️")
        unlink(filepath)
    
    @api.post("/upload")
    def upload_file():
        if "file" not in request.files:
            return jsonify({"error": "⚠️ No file part! ⚠️"}), HTTPStatus.BAD_REQUEST.value
        
        file = request.files["file"]
        
        if not file.filename:
            return jsonify({"error": "⚠️ No selected file! ⚠️"}), HTTPStatus.BAD_REQUEST.value
        
        if not allowed_file(file.filename):
            return jsonify({"error": "⚠️ Invalid file type. Only .py and .java files are allowed! ⚠️"}), HTTPStatus.BAD_REQUEST.value
        
        file_path = join(api.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)
        
        # Setting up the transpiler pro tem
        if file.filename.split(".")[-1].lower() == ALLOWED_EXTENSIONS[0]:
            transpiler: Transpiler = Transpiler(java_file=file_path).java2py()
        else:
            transpiler: Transpiler = Transpiler(python_file=file_path).py2js()
        
        print(f"\nFile: {file.filename} uploaded and transpiled!\n")
        
        return jsonify({"message": f"ℹ️ File: {file.filename} uploaded successfully! ℹ️"}), HTTPStatus.OK.value
    
    @api.get("/download/<filename>")
    def download_file(filename):
        try:
            return send_from_directory(api.config["UPLOAD_FOLDER"], filename, as_attachment=True)
        except FileNotFoundError:
            return jsonify({"error": "⚠️ File not found! ⚠️"}), HTTPStatus.BAD_REQUEST.value
    
    return api
