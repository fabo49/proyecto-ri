'''
Universidad de Costa Rica
Escuela de Ciencias de la Computacion e Informatica
CI-2414: Recuperacion de la informacion
Tarea programada 1
@author: Brayan Salas B26050
@author: Fabian Rodriguez B25695
'''
import os

# Se asume que desde donde se invoca es donde se maneja el tamano del buffer. [Como cuando se llena la memoria]
def SPIMI(token_stream, name):
	# Se utiliza open para crear el archivo donde va a estar el dictionary_file
	#ind_name = "index_%s.bin" % name
	if not os.path.exists("indices"): os.makedirs("indices")
	ind_name = "indices/index_%s.txt" %name
	index_file = open(ind_name,"wb")
	#dic_file = "dictionary_%s.bin" % name
	if not os.path.exists("directorios"): os.makedirs("directorios")
	dic_file = "diccionarios/dictionary_%s.txt" %name
	with open(dic_file,"wb") as dictionary_file:
		dictionary_terms = {}
		dictionary_freq = {}
		for token in token_stream:
			# pair[0] => token, pair[1] => doc_id
			term,doc_id = token[0],token[1]
			if term in dictionary_terms:
				posting_list = dictionary_terms[term]
				posting_freq = dictionary_freq[term]
			else:
				dictionary_terms[term] = []
				dictionary_freq[term] = []
				posting_list = dictionary_terms[term]
				posting_freq = dictionary_freq[term]

			# Busca si el documento se contabilizo para aumentar la frecuencia en ese doc en 1.
			if doc_id in posting_list:
				pos = posting_list.index(doc_id)
				posting_freq[pos] += 1
			else:	# Crea el cont de frecuencia con 1.
				posting_list.append(doc_id)
				posting_freq.append(1)

		# Ordenar los pares por el termino. lambda en python permite hacer una funcion anonima.
		sorted_terms = sorted(dictionary_terms, key=lambda pair: pair[0], reverse=False)
		for sorted_term in sorted_terms:
			pair_is = (sorted_term, dictionary_terms[sorted_term])
			#print('term: %s, doc_id: %s' % pair_is)

		writeIndexToDisk(sorted_terms, index_file)
		writeDicToDisk(dictionary_terms, dictionary_freq, dictionary_file)

	index_file.close()
	dictionary_file.close()
	#print 'Finaliza SPIMI'

def writeIndexToDisk(file, output):
	for f in file:
		f = f.encode('utf-8')
		output.write(f)
		output.write("\n")

def writeDicToDisk(file_1, file_2, output):
	for k,v in file_1.items():
		key = k.encode('utf-8')
		posting_list = v
		output.write(key)
		string = key
		string += ","
		string += str(v)
		print string
		posting_freq = file_2[k]
		act = 0
		for p in posting_list:
			freq = posting_freq[act]
			value = str(p).encode('utf-8')
			value += ":"
			value += str(freq)
			output.write("}k(*")
			output.write(value)
			output.write("\n")
			act += 1


# def writeBlockToDisk(file, output):
# 	# pickle permite guardar estructuras como binarios, para luego recuperarlas igual. cPickle es mas eficiente.
# 	try: from cPickle import HIGHEST_PROTOCOL, dump
# 	except: from pickle import HIGHEST_PROTOCOL, dump

# 	dump(file, output, HIGHEST_PROTOCOL)

# # Metodo que obtiene de un archivo la estructura original del mismo.
# def readBlockFromDisk(input_doc):	
# 	try: from cPickle import load
# 	except: from pickle import load

# 	with open(input_doc, 'rb') as inp:
# 		file = load(inp)
# 	inp.close()
# 	return file