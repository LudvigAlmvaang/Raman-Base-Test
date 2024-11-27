from flask import Blueprint, request, jsonify, redirect, url_for, current_app, session
import os

upload_bp = Blueprint('upload', __name__)

@upload_bp.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        files = request.files.getlist('files')

        if not files:
            return jsonify({'message': 'No file selected'}), 400

        session['uploaded_files'] = []

        for file in files:
            if file.filename == '':
                return jsonify({'message': 'One of the files has no filename'}), 400

            file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            session['uploaded_files'].append(file.filename)


    return redirect(url_for('plot'))