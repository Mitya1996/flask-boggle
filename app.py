from flask import Flask, render_template, request, session, redirect, jsonify
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

@app.route('/guess')
def guess():
    board = session['board']
    word = request.args['guess']
    result = boggle_game.check_valid_word(board, word)
    return jsonify({'response': result})

@app.route('/updateHighScore', methods=['GET', 'POST'])
def updateHighScore():
    session_HS = session.get('High Score', 0)
    if request.method == 'POST':
        new_HS = request.json['newHighScore']
        if new_HS > session_HS:
            session['High Score'] = new_HS

    return jsonify({'high_score': session_HS})
    

@app.route('/updateNumPlayed', methods=['GET', 'POST'])
def updateNumPlayed():
    session['num_played'] = session.get('num_played', 0) # initialize if not exist
    
    if request.method == 'POST':
        valid_increment = request.json['incrementOne']
        if valid_increment:
            session['num_played'] += 1 

    return jsonify({'num_played': session['num_played']})
    