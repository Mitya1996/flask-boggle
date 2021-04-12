from flask import Flask, render_template, request
from boggle import Boggle
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# the toolbar is only enabled in debug mode:
app.debug = True

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = 'trolol'

toolbar = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/')
def home():
    return render_template('home.html')