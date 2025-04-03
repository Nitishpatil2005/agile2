from flask import Flask, render_template, request
import os
from model import train_model

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html', accuracy=None, image_path=None)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Train model & get accuracy
    accuracy = train_model(file_path)
    
    return render_template('index.html', accuracy=round(accuracy * 100, 2), image_path="static/plot.png")

if __name__ == '__main__':
    app.run(debug=True)
