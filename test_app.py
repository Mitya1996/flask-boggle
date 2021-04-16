from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    # @classmethod
    # def setUpClass(cls):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        with self.client as client:

            test_game = Boggle()
            test_board = test_game.make_board()
            with client.session_transaction() as change_session:
                change_session['board'] = test_board

    def test_home(self):
        resp = self.client.get('/')
        html = resp.get_data(as_text=True)
        #check if status code 200
        self.assertEqual(resp.status_code, 200)
        #check if Boggle h1 is in the response
        self.assertIn('<h1>Boggle</h1>', html)

    def test_guess_ok(self):
        test_board =   [["C", "A", "T", "T", "T"], 
                        ["C", "A", "T", "T", "T"], 
                        ["C", "A", "T", "T", "T"], 
                        ["C", "A", "T", "T", "T"], 
                        ["C", "A", "T", "T", "T"]]
                        
        with self.client.session_transaction() as change_session:
            change_session['board'] = test_board
        
        resp = self.client.get('/guess?guess=cat') 
        message = resp.json['response']

        self.assertEqual("ok", message)
        self.assertEqual(resp.status_code, 200)

    def test_guess_not_word(self):

        resp = self.client.get('/guess?guess=asdf') #test a 'not-a-word'
        message = resp.json['response']

        self.assertEqual("not-word", message)
        self.assertEqual(resp.status_code, 200)

    def test_guess_not_on_board(self):

        resp = self.client.get('/guess?guess=helicopter') 
        message = resp.json['response']

        self.assertEqual("not-on-board", message)
        self.assertEqual(resp.status_code, 200)

