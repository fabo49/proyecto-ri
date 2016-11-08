'''
Universidad de Costa Rica
Escuela de Ciencias de la Computacion e Informatica
CI-2414: Recuperacion de la informacion
Tarea programada 1
@author: Brayan Salas B26050
@author: Fabian Rodriguez B25695
'''
import os
from HelpMethods import *

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

def EmpyFiles():
    '''
    Crea los archivos vacios que va a utilizar para guardar el indice y diccionario completo
    :return: un archivo "index.txt" vacio y otro archivo "dictionary.txt" vacio
    '''
    open('index.txt', 'w').close()
    open('dictionary.txt', 'w').close()

def UpdateFiles(index, dictionary):
    '''
    Metodo que sustituye el contenido del indice y del diccionario por los valores actualizados
    :param index: Lista con
    :param dictionary:
    :return:
    '''
    EmpyFiles()

    indice_final = open('index.txt', 'w')
    for term in index:
        indice_final.write(term)
    indice_final.close()


    diccionario_final = open('dictionary.txt', 'w')
    for term, list in dictionary.items():
        diccionario_final.write(term)
        for post in list:
            diccionario_final.write('}k(*'+ post.split()[0])
        diccionario_final.write('\n')
    diccionario_final.close()

def MergeBlocksHelper(indice_actual, diccionario_actual):
    '''
    Metodo ayudante de MergeBlocks que se encarga de hacer el merge entre el diccionario completo y el que esta leyendo.
    Necesita que existan los archivos "index.txt" y "dictionary.txt" en el directorio raiz
    :param indice_actual: el indice del bloque actual.
    :param diccionario_actual: el diccionario del bloque actual
    :return:
    '''

    # Guarda el indice completo en una lista
    indice = open('index.txt', 'r')
    indice_final = FileToList(indice)
    indice.close()

    # Guarda el diccionario en un "diccionario" con un key y una lista de ids
    diccionario = open('dictionary.txt', 'r')
    diccionario_final = FileToDictionary(diccionario)
    diccionario.close()

    if not indice_final: # Primer caso que el indice completo esta vacio, nada mas copia el primer indice en el indice completo
        indice = open('index.txt', 'a')
        for term in indice_actual:
            indice.write(term)
        indice.close()

        diccionario = open('dictionary.txt', 'a')
        for posting in diccionario_actual:
            diccionario.write(posting)
        diccionario.close()
    else:
        diccionario_tmp = FileToDictionary(diccionario_actual)   # Convierte el diccionario actual en un array asociativo
        for term in indice_actual:
            if term in indice_final: # El termino esta en el indice?
                term = term.split()[0]
                diccionario_final[term].extend(diccionario_tmp[term])
            else:   # No esta en el indice
                term = term.split()[0]  # Elimina el \n
                indice_final.append(term)    # Agrego el termino al indice
                diccionario_final[term] = diccionario_tmp[term]  # Agrego su posting list
        UpdateFiles(sorted(indice_final), diccionario_final) # Actualiza los documentos index.txt y dictionary.ext

    indice_actual.close()
    diccionario_actual.close()

def MergeBlocks():
    '''
    Metodo que se encarga de hacerle el merge de todos los bloques para crear un solo indice.
    :return: Un archivo con el indice completo
    '''
    EmpyFiles()
    index = 0
    for indice in os.listdir('indices'):
        MergeBlocksHelper(open("indices/"+indice, 'r'), open("diccionarios/dictionary_" + str(index) + ".txt", 'r'))
        index += 1


# Prueba
# MergeBlocks()