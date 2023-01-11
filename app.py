# Import libraries that we will use
from flask import Flask, render_template
import requests
import json


app = Flask(__name__)


def get_meme():
    with open('memes.json') as data_file:    
        data = json.load(data_file)
        return data['meme-title'], data['meme-url']
@app.route("/")
def index():
    meme_title, meme_url = get_meme()
    return render_template("index.html", meme_title=meme_title, meme_url=meme_url)

app.run(host="0.0.0.0", port=80)