'''
Universidad de Costa Rica
Escuela de Ciencias de la Computacion e Informatica
CI-2414: Recuperacion de la informacion
Tarea programada 1
@author: Brayan Salas B26050
@author: Fabian Rodriguez B25695
'''

from spimi import SPIMI

class doc():
	doc_id = ""
	url = ""

def main():
  # Recibe los tokens para procesar
  	# docs  = documentos
  	docs = os.walk(...)
	# tokens = getTokens(documento)
	tokens = {['process',]}
	# max_memory -> cantidad maxima de tokens "en memory"
	block = []
	max_memory = 5000

	# Se debe de buscar la forma de cargar cada archivo sin saber el total de docs
	for doc in docs:
		tokens = getTokens(doc)
		docId = doc.doc_id
		block += [(token,docId) for token in tokens]

	while len(block)!=0
		block += []
		try: total = SPIMI([block.pop() for x in xrange(max_memory)])
	except IndexError as ie: 
		pass
