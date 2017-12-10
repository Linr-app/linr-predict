from flask import Flask, jsonify, json, request
from sklearn import linear_model

class Fila:
    def __init__(self, tempo_medio_inicial):
        self.tempo_medio_inicial = tempo_medio_inicial
        self.training_count = 0
        self.regressor = linear_model.SGDRegressor()

app = Flask(__name__)

filas = {}

@app.route('/prediction/<int:ID>', methods=['GET'])
def prediction(ID):
    fila = filas[ID]
    if fila.training_count < 50:
        return jsonify({
            'status': 'ok',
	    'type': 0,
            'data': {
                'prediction': fila.tempo_medio_inicial
            },
        })
    return jsonify({
        'status': 'ok',
	'type' : 1,
        'data': {
            'prediction': fila.regressor.predict([
                [request.args["dia_da_semana"], request.args["hora_de_entrada"], int(request.form["posicao"])]
            ])
        },
    })

@app.route('/fit/<int:ID>', methods=['POST'])
def fit(ID):
    fila = filas[ID]
    fila.regressor.partial_fit([
            [int(request.form["dia_da_semana"]), int(request.form["hora_de_entrada"]), int(request.form["posicao"])]
        ],
        [int(request.form["tempo_de_espera_na_fila"])]
    )
    fila.training_count += 1
    return jsonify({
        'status': 'ok',
    })
    
@app.route('/register/<int:ID>', methods=['POST'])
def register(ID):
    tempo_medio_inicial = int(request.form['tempo_medio_inicial'])
    if ID not in filas:
        filas[ID] = Fila(tempo_medio_inicial)
        return jsonify({
            'status': 'ok',
        }), 201
    return jsonify({
        'status': 'error',
    })
       
if __name__ == '__main__':
    app.run(debug=True)

