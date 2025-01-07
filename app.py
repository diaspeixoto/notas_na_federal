from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dicionário de pesos
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
    ],
    # Adicione outras universidades e pesos aqui
    "Outra_Uni": [
        [3.0, 2.0, 1.0, 2.0, 2.0],
        [2.5, 2.5, 1.5, 2.0, 1.5],
    ],
}


@app.route("/")
def index():
    # Renderiza uma página HTML com o menu suspenso
    
    return render_template("index.html", universidades=pesos.keys())


@app.route("/calcular", methods=["POST"])
def calcular():
    # Recebe dados do formulário (notas e universidade)
    data = request.json
    universidade = data["universidade"]
    notas = list(map(float, data["notas"]))

    if universidade not in pesos:
        return jsonify({"error": "Universidade não encontrada!"}), 400

    # Calcula as notas ponderadas
    pesos_universidade = pesos[universidade]
    resultados = [
        sum(g1 * g2 for g1, g2 in zip(notas, grupo)) / 10
        for grupo in pesos_universidade
    ]

    maximo = max(resultados)
    grupo = resultados.index(maximo) + 1

    # Retorna os resultados
    return jsonify(
        {
            "resultados": resultados,
            "maximo": maximo,
            "grupo": grupo,
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
