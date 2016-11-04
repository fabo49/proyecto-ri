# import os # Para correr en C9
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/results")
def results():
	return "Estos son los resultados encontrados"

if __name__ == "__main__":
    app.run(debug=True,port=5052)
    # app.run(debug=True,host=os.environ['IP'],port=int(os.environ['PORT'])) # Para correr en C9
    