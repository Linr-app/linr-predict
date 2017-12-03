# linr-predict

FLASK:

## /prediction/<int: ID>, methods=['GET']

Parâmetros de link: ID_FILA
  
Parâmetros de POST: 

  dia_da_semana           // Entre (0-6), representa o dia da semana, 0 é segunda.
  
  hora_de_entrada         // Entre (0-1439), representa o minuto do dia, hora * 60 + minuto, 0 é 0:00.
  
Saída:

    if casos_teste < 50:
	'status': 'ok',
	'type': 0,
	'data': {
		'prediction': fila.tempo_medio_inicial // Segundos
	},
	// Nessa situação, é necessário multiplicar pela quantidade de pessoas na frente (fila.length * previsor * 60s-¹).
    else
	'status': 'ok',
	'type' : 1,
	'data': {
		'prediction': fila.regressor.predict([
		[request.args["dia_da_semana"], request.args["hora_de_entrada"]]
		])
	},


## /fit/<int: ID>, methods=['POST']

Parâmetros de link: ID_FILA
  
Parâmetros de POST: 

  dia_da_semana           // Entre (0-6), representa o dia da semana, 0 é segunda.
  
  hora_de_entrada         // Entre (0-1439), representa o minuto do dia, hora * 60 + minuto, 0 é 0:00.
  
  tempo_de_espera_na_fila // Segundos
  
Saída:

    return jsonify({
        'status': 'ok',
    })
    
    
## /register/<int: ID>, methods=['POST']

Parâmetros de link: ID_FILA
  
Parâmetros de POST: 

  tempo_medio_inicial // Tempo medio inicial, segundos.
  
Saída:

    if ID not in filas:
        Registra nova Fila
        return jsonify({
            'status': 'ok',
        }), 201
    else    
        return jsonify({
            'status': 'error',
        })   
