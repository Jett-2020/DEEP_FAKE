from flask import Flask, request, render_template, redirect, url_for, session
import os

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'supersecretkey'  

def delete_uploaded_files():
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

@app.route('/')
def home():
    if session.get('delete_files', True):
        delete_uploaded_files()
    session['delete_files'] = True
    return render_template('my.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'video' not in request.files:
        return redirect(url_for('home'))

    video_file = request.files['video']
    if video_file.filename == '':
        return redirect(url_for('home'))

    if video_file:
        
        _, file_extension = os.path.splitext(video_file.filename)
        
        new_filename = f'fake{file_extension}'
       
        full_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
      
        video_file.save(full_path)
      
        session['delete_files'] = False
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
