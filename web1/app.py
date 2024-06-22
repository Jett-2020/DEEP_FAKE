import os
from flask import Flask, request, jsonify ,render_template

from frame_analysis import send  # Ensure this is the correct import for your 'send' function

app = Flask(__name__)
# This will enable CORS for all routes
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

    # Analyze the video
    try:
        result = send()
        return jsonify({"message": result}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
