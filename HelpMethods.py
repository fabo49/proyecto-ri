'''
Universidad de Costa Rica
Escuela de Ciencias de la Computacion e Informatica
CI-2414: Recuperacion de la informacion
Tarea programada 1
@author: Brayan Salas B26050
@author: Fabian Rodriguez B25695
'''

from bs4 import BeautifulSoup  # Para parsear documentos HTML
from Documento import *
from LanguageProcessing import *
from spimiProcess import *
import os


class HelpMethods(object):
    '''
    Clase ayudante que tiene metodos intermedios entre las diferentes clases
    '''

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

    @staticmethod
    def MatrixDocuments():
        '''
        Metodo que hace un archivo que tiene el id del documento y su nombre
        :return: El archivo
        '''
        open('documents_index.txt', 'w').close()
        final_doc = open('documents_index.txt', 'a')
        id = 0
        for document in os.listdir('docs'):
            final_doc.write(str(id) + ',' + document + '\n')
            id += 1
        final_doc.close()

    @staticmethod
    def MatrixDocumentsToList():
        '''
        Convierte el archivo donde estan guardados los id's y nombres de los documentos a una lista
        :return:  La lista con los nombres de los documentos
        '''
        doc = open('documents_index.txt', 'r')
        final_list = []
        for line in doc:
            final_list.append(line.split(',')[1].split()[0])  # El ultimo split es para quitar el '\n'
        return final_list

    @staticmethod
    def ResultsList(id_list):
        '''
        Clase que crea una lista con objetos Documento a partir de una lista de id's
        :param id_list: lista con los id's de los documentos a convertir
        :return: Lista con objetos de tipo Documento
        '''
        documents_list = HelpMethods.MatrixDocumentsToList()  # Convierte el archivo donde estan los id's de los documentos y el nombre a una lista
        final_list = []
        for id in id_list:
            doc_id = id
            doc_name = documents_list[doc_id]
            soup = BeautifulSoup(open('docs/' + doc_name), "lxml")
            description = ""
            for meta in soup.head.find_all('meta'):
                if 'name' in meta.attrs and 'content' in meta.attrs and meta.attrs['name'] == "description":
                    description = meta.attrs['content']
                    description = description[:200] + (description[200:] and '..')
                    break
                else:
                    paragraph = soup.find('p').get_text()
                    description = paragraph[:200] + (paragraph[200:] and '..')
            document_tmp = Documento(doc_id, str(doc_name).replace('.html', '', 1).replace('|', '/'),
                                     soup.title.string if soup.title else '',
                                     description)
            final_list.append(document_tmp)
        return final_list

    @staticmethod
    def TokenizeQuery(query):
        '''
        Metodo que se encarga de parsear y tokenizar la consulta que realiza el usuario.
        :param query: la consulta que realiza el usuario
        :return: una lista con los tokens de la consulta
        '''

        return LanguageProcessing.Tokenize(query, True)  # Se eliminan los Stop-Words de la consulta y se tokeniza

    @staticmethod
    def CreateIndexAndDictionary():
        '''
        Metodo que genera el Indice y el diccionario general con base en los documentos que obtuvo el crawler.
        :return:
        '''

        doc_id = 0
        for document in os.listdir('docs'):
            clean_doc = LanguageProcessing.CleanHTML(
                'docs/' + document)  # Elimina tags de html y la seccion de javascript
            clean_doc = LanguageProcessing.Tokenize(clean_doc, True)  # Tokeniza y elimina stop-words
            posting_list = []
            for token in clean_doc:
                posting_list.append((token, doc_id))
            SpimiProcess.Spimi(posting_list, 1400)
            doc_id += 1
        SpimiProcess.MergeBlocks()
