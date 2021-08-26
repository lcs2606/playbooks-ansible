from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Versão 4 - Agora vai</p>"
