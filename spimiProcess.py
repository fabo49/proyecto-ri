'''
Universidad de Costa Rica
Escuela de Ciencias de la Computacion e Informatica
CI-2414: Recuperacion de la informacion
Tarea programada 1
@author: Brayan Salas B26050
@author: Fabian Rodriguez B25695
'''
import os

class SpimiProcess(object):
    '''
    Clase encargada de realizar todos los pasos del algoritmo de SPIMI
    '''

    @staticmethod
    def Spimi(posting_list, buffer_size):
        '''
        Metodo que hace el llamado a Spimi pero le define el tamano del buffer de la memoria.
        :param posting_list: La lista con los postings
        :param buffer_size: El tamano del buffer en memoria que va a utilizar Spimi
        :return:
        '''
        postings = posting_list
        file_name = 0
        while len(postings) != 0:
            try:
                leng = 0
                if len(postings) < buffer_size:
                    leng = len(postings)
                else:
                    leng = buffer_size
                SpimiProcess.SpimiHelper([postings.pop(0) for x in xrange(leng)], file_name)
            except IndentationError as ie:
                pass
            file_name += 1

    @staticmethod
    def SpimiHelper(token_stream, name):
        # Se asume que desde donde se invoca es donde se maneja el tamano del buffer. [Como cuando se llena la memoria]
        # Se utiliza open para crear el archivo donde va a estar el dictionary_file
        # ind_name = "index_%s.bin" % name
        if not os.path.exists("indices"): os.makedirs("indices")
        ind_name = "indices/index_%s.txt" % name
        index_file = open(ind_name, "wb")
        # dic_file = "dictionary_%s.bin" % name
        if not os.path.exists("diccionarios"): os.makedirs("diccionarios")
        dic_file = "diccionarios/dictionary_%s.txt" % name
        with open(dic_file, "wb") as dictionary_file:
            dictionary_terms = {}
            dictionary_freq = {}
            for token in token_stream:
                # pair[0] => token, pair[1] => doc_id
                term, doc_id = token[0], token[1]
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
                else:  # Crea el cont de frecuencia con 1.
                    posting_list.append(doc_id)
                    posting_freq.append(1)

            # Ordenar los pares por el termino. lambda en python permite hacer una funcion anonima.
            sorted_terms = sorted(dictionary_terms, key=lambda pair: pair[0], reverse=False)
            for sorted_term in sorted_terms:
                pair_is = (sorted_term, dictionary_terms[sorted_term])
            # print('term: %s, doc_id: %s' % pair_is)

            SpimiProcess.WriteIndexToDisk(sorted_terms, index_file)
            SpimiProcess.WriteDicToDisk(dictionary_terms, dictionary_freq, dictionary_file)

        index_file.close()
        dictionary_file.close()

    @staticmethod
    def WriteIndexToDisk(file, output):
        for f in file:
            f = f.encode('utf-8')
            output.write(f)
            output.write("\n")

    @staticmethod
    def WriteDicToDisk(file_1, file_2, output):
        for k, v in file_1.items():
            key = k.encode('utf-8')
            posting_list = v
            output.write(key)
            string = key
            string += ","
            string += str(v)
            # print string
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

    @staticmethod
    def EmpyFiles():
        '''
        Crea los archivos vacios que va a utilizar para guardar el indice y diccionario completo
        :return: un archivo "index.txt" vacio y otro archivo "dictionary.txt" vacio
        '''
        open('index.txt', 'w').close()
        open('dictionary.txt', 'w').close()

    @staticmethod
    def UpdateFiles(index, dictionary):
        '''
        Metodo que sustituye el contenido del indice y del diccionario por los valores actualizados
        :param index: Lista con
        :param dictionary:
        :return:
        '''
        SpimiProcess.EmpyFiles()

        indice_final = open('index.txt', 'w')
        for term in index:
            indice_final.write(term.split()[0])
            indice_final.write('\n')
        indice_final.close()

        diccionario_final = open('dictionary.txt', 'w')
        for term, list in dictionary.items():
            diccionario_final.write(term)
            for post in list:
                diccionario_final.write('}k(*' + post.split()[0])
            diccionario_final.write('\n')
        diccionario_final.close()

    @staticmethod
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
        indice_final = SpimiProcess.FileToList(indice)
        indice.close()

        # Guarda el diccionario en un "diccionario" con un key y una lista de ids
        diccionario = open('dictionary.txt', 'r')
        diccionario_final = SpimiProcess.FileToDictionary(diccionario)
        diccionario.close()

        if not indice_final:  # Primer caso que el indice completo esta vacio, nada mas copia el primer indice en el indice completo
            indice = open('index.txt', 'a')
            for term in indice_actual:
                indice.write(term)
            indice.close()

            diccionario = open('dictionary.txt', 'a')
            for posting in diccionario_actual:
                diccionario.write(posting)
            diccionario.close()
        else:
            diccionario_tmp = SpimiProcess.FileToDictionary(
                diccionario_actual)  # Convierte el diccionario actual en un array asociativo
            for term in indice_actual:
                if term in indice_final:  # El termino esta en el indice?
                    term = term.split()[0]
                    diccionario_final[term].extend(diccionario_tmp[term])
                else:  # No esta en el indice
                    term = term.split()[0]  # Elimina el \n
                    indice_final.append(term)  # Agrego el termino al indice
                    diccionario_final[term] = diccionario_tmp[term]  # Agrego su posting list
            SpimiProcess.UpdateFiles(sorted(indice_final),
                                     diccionario_final)  # Actualiza los documentos index.txt y dictionary.ext

        indice_actual.close()
        diccionario_actual.close()

    @staticmethod
    def MergeBlocks():
        '''
        Metodo que se encarga de hacerle el merge de todos los bloques para crear un solo indice.
        :return: Un archivo con el indice completo
        '''
        SpimiProcess.EmpyFiles()
        index = 0
        for indice in os.listdir('indices'):
            SpimiProcess.MergeBlocksHelper(open("indices/" + indice, 'r'),
                                           open("diccionarios/dictionary_" + str(index) + ".txt", 'r'))
            index += 1

    @staticmethod
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

    @staticmethod
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
