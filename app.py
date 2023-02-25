from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from wtforms.validators import DataRequired
import os
from mutagen.mp3 import MP3
import mysql.connector as mysql


app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'



@app.route("/upload")
def up():
    return render_template('upload.html')



@app.route("/searchs")
def searchs():
    return render_template('search.html')


'''class UploadForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    artist = StringField('Artist', validators=[DataRequired()])
    album = StringField('Album', validators=[DataRequired()])
    mp3_file = FileField('MP3 file', validators=[DataRequired()])'''
@app.route("/view")
def display_songs():
    conn = mysql.connect(host='localhost',user='root',password='Ksb6419*',database='songs')
    cur = conn.cursor()
    cur.execute("SELECT title, artist, album FROM songs")
    songs = cur.fetchall()
    conn.close()
    return render_template("viewallsongs.html", songs=songs)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search_query = request.form["search_query"]
        conn = mysql.connect(host='localhost',user='root',password='Ksb6419*',database='songs')
        cur = conn.cursor()
        cur.execute("SELECT title, artist, album FROM songs WHERE title LIKE ? OR artist LIKE ? OR album LIKE ?", ("%" + search_query + "%", "%" + search_query + "%", "%" + search_query + "%"))
        songs = cur.fetchall()
        conn.close()
        return render_template("search.html", songs=songs, search_query=search_query)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

    
