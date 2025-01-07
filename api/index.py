from flask import Flask, request, jsonify

app = Flask(__name__)

pesos = {
    "UFG": [
        [2.0, 1.0, 2.5, 3.0, 1.5],
        [2.0, 1.0, 1.5, 4.0, 1.5],
        [2.0, 1.0, 1.0, 4.0, 2.0],
        [2.0, 1.5, 3.0, 1.5, 2.0],
        [2.0, 2.0, 3.0, 1.5, 2.0],
        [2.5, 3.0, 1.0, 1.0, 2.5],
        [2.5, 2.0, 1.0, 2.0, 2.5],
        [3.0, 2.5, 1.0, 1.0, 2.5],
    ]
}

@app.route("/calcular", methods=["POST"])
def calcular():
    data = request.json
    notas = data.get("notas")
    universidade = data.get("universidade")
    
    if not notas or not universidade:
        return jsonify({"error": "Dados incompletos"}), 400

    if universidade not in pesos:
        return jsonify({"error": "Universidade não encontrada"}), 404

    resultado = [
        sum(g1 * g2 for g1, g2 in zip(notas, y)) / 10 for y in pesos[universidade]
    ]

    maximo = max(resultado)
    grupo = resultado.index(maximo) + 1

    return jsonify({"maior_nota": maximo, "grupo": grupo})

if __name__ == "__main__":
    app.run()
