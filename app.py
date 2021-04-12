from flask import Flask, render_template, request, session
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
    if not session.get('board', None):               #unless it already exists
        session['board'] = boggle_game.make_board()  #create a 5x5 board in flask session cookie 

    return render_template('home.html', boggle_game=boggle_game)