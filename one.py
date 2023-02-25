from flask import Flask,render_template,redirect,request,send_file,send_from_directory
from flask_wtf import FlaskForm
import os
from fileinput import filename
import urllib.request
from werkzeug.utils import secure_filename

'''
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from wtforms.validators import DataRequired
import os
from mutagen.mp3 import MP3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

class UploadForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    artist = StringField('Artist', validators=[DataRequired()])
    album = StringField('Album', validators=[DataRequired()])
    mp3_file = FileField('MP3 file', validators=[DataRequired()])
@app.route('/', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        # Save the uploaded file
        mp3_file = form.mp3_file.data
        mp3_filename = mp3_file.filename
        mp3_file.save(mp3_filename)

        # Read the metadata
        audio = MP3(mp3_filename)
        title = form.title.data or audio.get("TIT2", "Unknown Title")
        artist = form.artist.data or audio.get("TPE1", "Unknown Artist")
        album = form.album.data or audio.get("TALB", "Unknown Album")

        # Create a folder for the metadata if it doesn't exist
        folder_name = os.path.join(title, artist, album)
        os.makedirs(folder_name, exist_ok=True)

        # Move the uploaded file to the folder
        new_path = os.path.join(folder_name, mp3_filename)
        os.rename(mp3_filename, new_path)

        return 'File uploaded successfully!'
    return render_template('upload.html', form=form)



'''


#initialization...
app=Flask(__name__)
UPLOAD_FOLDER='music'
app.secret_key='1111'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
ALLOWED_EXTENSIONS=set(['.mp3','.jpg'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


'''

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def display_songs():
    conn = sqlite3.connect("songs.db")
    cur = conn.cursor()
    cur.execute("SELECT title, artist, album FROM songs")
    songs = cur.fetchall()
    conn.close()
    return render_template("songs.html", songs=songs)

if __name__ == "__main__":
    app.run(debug=True)


'''


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
    




    '''
    
    from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search_query = request.form["search_query"]
        conn = sqlite3.connect("songs.db")
        cur = conn.cursor()
        cur.execute("SELECT title, artist, album FROM songs WHERE title LIKE ? OR artist LIKE ? OR album LIKE ?", ("%" + search_query + "%", "%" + search_query + "%", "%" + search_query + "%"))
        songs = cur.fetchall()
        conn.close()
        return render_template("search.html", songs=songs, search_query=search_query)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

    
    
    '''