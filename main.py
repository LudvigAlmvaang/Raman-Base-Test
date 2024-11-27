from flask import Flask, render_template, session
from upload import upload_bp
from plot import create_plot
import os
import secrets

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.secret_key = secrets.token_hex(16)
app.register_blueprint(upload_bp)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot')
def plot():
    uploaded_files = session.get('uploaded_files', [])

    upload_folder = app.config['UPLOAD_FOLDER']
    file_paths = [os.path.join(upload_folder, filename) for filename in uploaded_files]

    plot_div = create_plot(*file_paths)
    return render_template('plot.html', plot_div=plot_div, files=uploaded_files)

if __name__ == '__main__':
    app.run(debug=True)