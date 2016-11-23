'''
Universidad de Costa Rica
Escuela de Ciencias de la Computacion e Informatica
CI-2414: Recuperacion de la informacion
Tarea programada 1
@author: Brayan Salas B26050
@author: Fabian Rodriguez B25695
'''

# import os # Para correr en C9
from flask import Flask, render_template, request, jsonify
from datetime import datetime
import Documento
from HelpMethods import *
from scoring import *
from Ad import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/_update_views')
def UpdateViews():
    link = request.args.get('ad')
    ad = Ad.GetAd(link)
    ad.UpdateAd()
    return jsonify(url=link)


@app.route('/confirmAd', methods=['POST'])
def SaveAd():
    new_ad = Ad(request.form['ad_title'], request.form['ad_description'], request.form['ad_url'],
                request.form['ad_keywords'], request.form['ad_payment_options'])
    new_ad.SaveAd()
    return render_template('adConfirm.html', ad=new_ad)


@app.route('/createAd/', methods=['GET'])
def CreateAd():
    return render_template('createAd.html')


@app.route('/results/')
@app.route('/results/', methods=['GET'])
def results():
    query = request.args.get('query')
    t_inicial = datetime.now()  # Empieza a tomar el tiempo
    results_list = Scoring.Score(query, 'index.txt', 'dictionary.txt', False)
    documents_list = HelpMethods.ResultsList(results_list)
    t_final = datetime.now() - t_inicial  # Hace el calculo del tiempo que le tomo hacer la consulta
    ads = Ad.Ads()  # Por ahora muestra todos los anuncios que hay
    return render_template('results.html', query=query, time=t_final, documents=documents_list,
                           cant_results=len(documents_list), ads=ads)


if __name__ == "__main__":
    HelpMethods.MatrixDocuments()
    print '[DEBUG]: Indexando...'
    HelpMethods.CreateIndexAndDictionary()
    app.run(debug=True, port=5052)
    # app.run(debug=True,host=os.environ['IP'],port=int(os.environ['PORT'])) # Para correr en C9
