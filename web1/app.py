import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from frame_analysis import send

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = './'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify({"message": "No video file part"}), 400
    
    file = request.files['video']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
    
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'fake.mp4')
    file.save(file_path)

    return jsonify({"message": "Video uploaded successfully."}), 200

@app.route('/analyze', methods=['POST'])
def analyze_video():
    try:
        result = send()
        return jsonify({"message": result}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
