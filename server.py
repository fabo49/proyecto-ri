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
import Documento
from HelpMethods import *
from scoring import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/results/')
@app.route('/results/', methods=['GET'])
def results():
    query = request.args.get('query')
    t_inicial = datetime.now().second  # Empieza a tomar el tiempo
    results_list = Scoring.Score(query, 'index.txt', 'dictionary.txt', False)
    documents_list = HelpMethods.ResultsList(results_list)
    t_final = datetime.now().second - t_inicial  # Hace el calculo del tiempo que le tomo hacer la consulta
    return render_template('results.html', query=query, time=t_final, documents=documents_list,
                           cant_results=len(documents_list))


if __name__ == "__main__":
    # Aca hay que llamar el crawler, generar el indice y el diccionario
    # Para llamar al crawler y matarlo despues de cierto tiempo: http://stackoverflow.com/questions/14920384/stop-code-after-time-period
    HelpMethods.MatrixDocuments()
    print '[DEBUG]: Indexando...'
    HelpMethods.CreateIndexAndDictionary()
    app.run(debug=True, port=5052)
    # app.run(debug=True,host=os.environ['IP'],port=int(os.environ['PORT'])) # Para correr en C9
