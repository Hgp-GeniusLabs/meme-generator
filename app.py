# Import libraries that we will use
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# This is how we initiate a flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
db = SQLAlchemy()
db.init_app(app)

# Create the meme model 
class Meme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img_src = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


# This function will load our website naked. Meaning nothing behind the /. 
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        meme_content = request.form['content']
        new_meme = Meme(content=meme_content)

        try:
            db.session.add(new_meme)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your Meme'

    else:
        memes = Meme.query.order_by(Meme.date_created).all()
        return render_template('index.html', memes=memes)


# This line will run our server on this port 80
if (__name__ == "__main__"):
    app.run(host="0.0.0.0", port=80)



# YOUR GOAL IS TO ADD MORE MEMES AND SHOW THEM ALL IN THE PAGE USING A LOOP

