'''
Universidad de Costa Rica
Escuela de Ciencias de la Computacion e Informatica
CI-2414: Recuperacion de la informacion
Tarea programada 1
@author: Brayan Salas B26050
@author: Fabian Rodriguez B25695
'''

# import os # Para correr en C9
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/results/')
@app.route('/results/', methods=['GET'])
def results():
    t_inicial = datetime.now().microsecond
    # Hacer la logica de la busqueda
    i = 0
    for i in xrange(20000):
        print "[CICLO TONTO]: es nada mas para ver tiempo."

    t_final = datetime.now().microsecond - t_inicial
    return render_template('results.html', query=request.args.get('query'), time=t_final)


if __name__ == "__main__":
    # Aca hay que llamar el crawler, generar el indice y el diccionario
    app.run(debug=True, port=5052)
    # app.run(debug=True,host=os.environ['IP'],port=int(os.environ['PORT'])) # Para correr en C9
