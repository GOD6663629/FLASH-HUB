from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")  # Homepage

@app.route('/blackjack')
def blackjack():
    return render_template("blackjack.html")  # Blackjack game

@app.route('/xando')
def tic_tac_toe():
    return render_template("xando.html")  # Tic-Tac-Toe

@app.route('/guessnumber')
def guess_number():
    return render_template("guessnumber.html")  # Guess the Number

@app.route('/hangman')
def hangman():
    return render_template("hangman.html")  # Hangman game

@app.route('/calculator')
def calculator():
    return render_template("calculator.html")  # Calculator

if __name__ == "__main__":
    app.run(debug=True)