from flask import Flask, jsonify

app = Flask(__name__)

jogos = [
    {"id": 1, "nome": "Genshin impact"},
    {"id": 2, "nome": "Honkai impact"},
    {"id": 3, "nome": "stardew valley"},
]

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(jogos)

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    novo = request.json
    novo['id'] = len(jogos) + 1
    jogos.append(novo)
    return jsonify(novo), 201

if __name__ == '__main__':
    app.run(debug=True)