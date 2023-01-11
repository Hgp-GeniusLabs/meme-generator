# Import libraries that we will use
from flask import Flask, render_template
import json


# This is how we initiate a flask app
app = Flask(__name__)


# This function will load our json file 
# and return both meme-title and meme-url
def get_meme():
    with open('memes.json') as data_file:    
        data = json.load(data_file)
        return data['meme-title'], data['meme-url']


# This function will load our website naked. Meaning nothing behind the /. 
@app.route("/")
def index():
    meme_title, meme_url = get_meme()
    return render_template("index.html", meme_title=meme_title, meme_url=meme_url)


# This line will run our server on this port 80
app.run(host="0.0.0.0", port=80)