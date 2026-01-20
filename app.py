from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Bonjour tout le monde, Je suis Jojo, votre ami de tous les jours. Je vous aime fort. Bisoussssss"

if __name__ == "__main__":
    app.run()
