from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    def test_home(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)
            #check if status code 200
            self.assertEqual(resp.status_code, 200)
            #check if Boggle h1 is in the response
            self.assertIn('<h1>Boggle</h1>', html)

    def test_guess(self):
        with app.test_client() as client:
            test_game = Boggle()
            board = test_game.make_board()

            with client.session_transaction() as change_session:
                change_session['board'] = board
            resp = client.get('/guess?guess=asdf') #test a 'not-a-word'
            message = resp.get_data()
            self.assertIn("not-word", message)