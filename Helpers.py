'''
Universidad de Costa Rica
Escuela de Ciencias de la Computacion e Informatica
CI-2414: Recuperacion de la informacion
Tarea programada 1
@author: Brayan Salas B26050
@author: Fabian Rodriguez B25695
'''

class Helpers(object):

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
