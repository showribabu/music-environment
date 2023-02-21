from flask import Flask,render_template,redirect,request,send_file,send_from_directory
from flask_wtf import FlaskForm
import os
from fileinput import filename
import urllib.request
from werkzeug.utils import secure_filename


#initialization...
app=Flask(__name__)
UPLOAD_FOLDER='music'
app.secret_key='1111'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
ALLOWED_EXTENSIONS=set(['.mp3','.jpg'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS





#handlers....

@app.route('/')
def dis():
    return render_template('index.html')

@app.route('/file',methods=['post'])
def file():
    if 'file' not in request.files:
        return render_template('index.html',f=" file Not Avilable")
    file=request.files['file']
    if file.filename == '':
        return render_template('index.html',f='No image selected for uploading')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        #here file secure with its name...
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #file_url=url_for('get_file',filename=filename)
        print('upload_image filename: ' + filename)

    else:
        return render_template('index.html',f="'Allowed image types are - png, jpg, jpeg, gif'")
    


#start...
if __name__=='__main__':
    app.run(debug=True)
    