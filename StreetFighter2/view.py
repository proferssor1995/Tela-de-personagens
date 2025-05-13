from main import app

@app.route("/")
def homepage():
    return "Bem vindo no FLask"

@app.route("/blog")
def blog():
    return "Bem-vindo"