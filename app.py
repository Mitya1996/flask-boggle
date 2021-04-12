from flask import Flask, render_template, request, session, redirect
from boggle import Boggle
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# the toolbar is only enabled in debug mode:
app.debug = True

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = 'trolol'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/')
def home():
    if not session.get('board', None):               #unless it already exists
        session['board'] = boggle_game.make_board()  #create a 5x5 board in flask session cookie 

    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guesss():
    print(request.form['word'])
    return redirect('/')