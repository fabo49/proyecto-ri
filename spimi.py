'''
Universidad de Costa Rica
Escuela de Ciencias de la Computacion e Informatica
CI-2414: Recuperacion de la informacion
Tarea programada 1
@author: Brayan Salas B26050
@author: Fabian Rodriguez B25695
'''

# Se asume que desde donde se invoca es donde se maneja el tamaño del buffer. [Como cuando se llena la memoria]
def SPIMI(token_stream):
	# Se utiliza open para crear el archivo donde va a estar el output_file
	with open("spimi.bin","wb") as output_file:
		dictionary = {}
		for token in token_stream:
			# pair[0] => token, pair[1] => doc_id
			pair = [token[0],token[1]]
			if pair[0] is not dictionary:
				posting_list = addToDictionary(dictionary,pair[0])
			else:
				posting_list = getPostingList(dictionary,pair[0])
			addToPostingsList(posting_list,pair[1])
		# Ordenar los pares por el término. lambda en python permite hacer una funcion anónima.
		sorted_terms = sorted(dictionary, key=lambda pair: pair[0], reverse=True)
		writeBlockToDisk(sorted_terms, output_file)
		writeBlockToDisk(dictionary, output_file)
	output_file.close()

def addToDictionary(dictionary, term):
	dictionary[term] = []
	return dictionary[term]

def getPostingsList(dictionary, term): 
	return dictionary[term]	

def addToPostingsList(postings_list, doc_id): 
	if doc_id not in postings_list:
		postings_list.insert(0,doc_id) # Inserta en el inicio de la lista, la posicion que siempre vamos a conocer.

def writeBlockToDisk(file, output):
	# pickle permite guardar estructuras como binarios, para luego recuperarlas igual. cPickle es más eficiente.
	try: from cPickle import HIGHEST_PROTOCOL,dump
	except: from pickle import HIGHEST_PROTOCOL,dump

	dump(file, output_file, HIGHEST_PROTOCOL)

# Metodo que obtiene de un archivo la estructura original del mismo.
def readBlockFromDisk(input):	
	try: from cPickle import load
	except: from pickle import load

	open(input, 'rb') as inp:
		file = load(inp)
	inp.close()
	return file