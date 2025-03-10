from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")  # Your game menu

@app.route('/blackjack')
def blackjack():
    return render_template("blackjack.html")  # Your blackjack game

@app.route('/xando')
def tic_tac_toe():
    return render_template("xando.html")  # Your Tic-Tac-Toe game

if __name__ == "__main__":
    app.run(debug=True)