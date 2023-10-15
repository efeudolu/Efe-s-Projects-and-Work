from flask import Flask, render_template
from module import roll_dice, player_turn, computer_turn, play_game

app = Flask(__name__)


@app.route('/')
def home():
    message = "Hello!"
    return render_template('website-for-game.html', message=message)

def index():
    print(" === Welcome to Efe's Game of Pig! ===")

@app.route('/about')
def about():
    print("Here are the rules of the game.")
    print("This a simple decision making game which includes one die, a player and a computer.")
    print("The player starts the game, and you can either choose to roll or hold the die.")
    print("If you roll a number above one, you can roll again or hold.")
    print("If you roll again, but roll a one, you lose all points for that turn, and your turn is over.")
    print("If you choose to hold, the points you have accumulated during that turn will be saved, and your turn is over.")
    print("The winner of the game is whoever reaches 100 points first.")

@app.route('/play')
def play():
    game_result = play_game()
    return render_template('game.html', result=game_result)

if __name__ == '__main__':
    app.run(debug=True)
