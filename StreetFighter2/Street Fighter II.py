from flask import Flask, jsonify, request

app = Flask(__name__)



personagens = [
    {
        'id': 1,
        'nome' : 'Ryu',
        'sexo':'homem',
        'nacionalidade': 'Japão',
    },   
    {
        'id': 2,
        'nome' : 'Ken',
        'sexo':'homem',
        'nacionalidade': 'Estados Unidos',
    }
]

@app.route('/personagens', methods=['GET'])
def obter_personagens():
    return jsonify(personagens)

@app.route('/personagens/<int:id>', methods=['GET'])
def obter_personagem_por_id(id):
    for personagem in personagens:
        if personagem.get('id') == id:
            return jsonify(personagem)
    return jsonify({'erro': 'Personagem não encontrado'}), 404

@app.route('/personagens/<int:id>', methods=['PUT'])
def editar_personagens_por_id(id):
    personagem_alterado = request.get_json()
    for indice, personagem in enumerate(personagens):
        if personagem.get('id') == id:
            personagens[indice].update(personagem_alterado)
            return jsonify(personagens[indice])  # <- corrigido aqui também
    return jsonify({'erro': 'Personagem não encontrado'}), 404

@app.route('/personagens',methods=['POST'])
def incluir_novo_personagem():
    novo_personagem = request.get_json()
    personagens.append(novo_personagem)
    return jsonify(personagens)

if __name__ == '__main__':
    app.run()