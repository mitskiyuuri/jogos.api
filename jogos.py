from flask import Flask, jsonify

app = Flask(__name__)

jogos = [
    {"id": 1, "nome": "Genshin impact"},
    {"id": 2, "nome": "Honkai impact"},
    {"id": 3, "nome": "stardew valley"},
]

@app.route("/jogos", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de Jogos - Acesse /jogos"})

@app.route("/", methods=["GET"])
def listar_jogos():
    return jsonify(jogos)

if __name__ == "__main__":
    app.run(port=5001)
