from app import app
from app.models.player import Player
from app.models.game import Game
from flask import render_template


@app.route('/<choice1>/<choice2>')
def play(choice1, choice2):
    player1 = Player("Steve", choice1)
    player2 = Player("Scott", choice2)
    game = Game()
    winner = game.play_game(player1.choice, player1.name, player2.choice, player2.name)

    return render_template('index.html', player1=player1, player2=player2, winner=winner)