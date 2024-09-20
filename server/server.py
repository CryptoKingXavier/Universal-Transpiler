from logging import info
from http import HTTPStatus
from threading import Thread
from secrets import token_hex
from os import makedirs, unlink
from os.path import exists, join
from transpile import Transpiler
from flask import Flask, jsonify, request, send_from_directory


def create_app() -> Flask:
    api: Flask = Flask(__name__)
    api.secret_key  = token_hex(16)
    
    # Configure upload folder
    UPLOAD_FOLDER = "./database"
    makedirs(UPLOAD_FOLDER) if not exists(UPLOAD_FOLDER) else None
    
    api.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    
    # Allowed file extensions
    ALLOWED_EXTENSIONS = ["java", "py"]
    
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
        finally:
            thread: Thread = Thread(target=unzip(join(api.config["UPLOAD_FOLDER"], filename)))
            thread.start()
    
    return api

