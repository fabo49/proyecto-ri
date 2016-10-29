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
    ind_name = "index_%s.bin" % name
    index_file = open(ind_name, "wb")
    dic_file = "dictionary_%s.bin" % name
    with open(dic_file, "wb") as dictionary_file:
        dictionary = {}
        for token in token_stream:
            # pair[0] => token, pair[1] => doc_id
            term, doc_id = token[0], token[1]
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
        # print('term: %s, doc_id: %s' % pair_is)

        writeBlockToDisk(sorted_terms, index_file)
        writeBlockToDisk(dictionary, dictionary_file)
    index_file.close()
    dictionary_file.close()


# print 'Finaliza SPIMI'

def writeBlockToDisk(file, output):
    # pickle permite guardar estructuras como binarios, para luego recuperarlas igual. cPickle es mas eficiente.
    try:
        from cPickle import HIGHEST_PROTOCOL, dump
    except:
        from pickle import HIGHEST_PROTOCOL, dump

    dump(file, output, HIGHEST_PROTOCOL)


# Metodo que obtiene de un archivo la estructura original del mismo.
def readBlockFromDisk(input_doc):
    try:
        from cPickle import load
    except:
        from pickle import load

    with open(input_doc, 'rb') as inp:
        file = load(inp)
    inp.close()
    return file


def FileToList(file):
    '''
    Metodo ayudante que convierte un archivo de texto con el indice en una lista.
    :param file: el archivo a convertir en lista
    :return: la lista de terminos
    '''
    lista = []
    for line in file:
        lista.append(line)
    return lista

def FileToDictionary(file):
    '''
    Metodo ayudante que convierte un archivo de texto con el diccionario a un diccionario de python
    :param file: el archivo que desea convertir
    :return: un array asociativo con el key el termino y de value una lista con los ids de los documentos
    '''
    dictionary = {}
    for line in file:
        posting = line.split('}k(*')
        dictionary[posting.pop(0)] = posting
    return dictionary

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
                diccionario_final[term].extend(diccionario_tmp[term.split()[0]])
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
