'''
Universidad de Costa Rica
Escuela de Ciencias de la Computacion e Informatica
CI-2414: Recuperacion de la informacion
Tarea programada 1
@author: Brayan Salas B26050
@author: Fabian Rodriguez B25695
'''

# Se asume que desde donde se invoca es donde se maneja el tamano del buffer. [Como cuando se llena la memoria]
def SPIMI(token_stream, dic_name):
	# Se utiliza open para crear el archivo donde va a estar el dictionary_file
	index_file = open("index.bin","wb")
	dic_file = "dictionary_%s.bin" % dic_name
	with open(dic_file,"wb") as dictionary_file:
		dictionary = {}
		for token in token_stream:
			# pair[0] => token, pair[1] => doc_id
			term,doc_id = token[0],token[1]
			if term in dictionary:
				posting_list = dictionary[term]
			else:
				dictionary[term] = []
				posting_list = dictionary[term]
			posting_list.append(doc_id)

		# Ordenar los pares por el termino. lambda en python permite hacer una funcion anonima.
		sorted_terms = sorted(dictionary, key=lambda pair: pair[0], reverse=False)
		for sorted_term in sorted_terms:
			pair_is = (sorted_term, dictionary[sorted_term])
			print('term: %s, doc_id: %s' % pair_is)

		writeBlockToDisk(sorted_terms, index_file)
		writeBlockToDisk(dictionary, dictionary_file)
	index_file.close()
	dictionary_file.close()
	print 'Finaliza SPIMI'

def writeBlockToDisk(file, output):
	# pickle permite guardar estructuras como binarios, para luego recuperarlas igual. cPickle es mas eficiente.
	try: from cPickle import HIGHEST_PROTOCOL, dump
	except: from pickle import HIGHEST_PROTOCOL, dump

	dump(file, output, HIGHEST_PROTOCOL)

# Metodo que obtiene de un archivo la estructura original del mismo.
def readBlockFromDisk(input_doc):	
	try: from cPickle import load
	except: from pickle import load

	with open(input_doc, 'rb') as inp:
		file = load(inp)
	inp.close()
	return file