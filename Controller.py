'''
Universidad de Costa Rica
Escuela de Ciencias de la Computacion e Informatica
CI-2414: Recuperacion de la informacion
Tarea programada 1
@author: Brayan Salas B26050
@author: Fabian Rodriguez B25695
'''

from LanguageProcessing import *
from spimiProcess import SPIMI
from bs4 import BeautifulSoup  # Para parsear documentos HTML
from Documento import *
import os


class Controller(object):
    '''
    Clase que se encarga de controlar las acciones que se tienen que realizar por el programa.
    '''

    @staticmethod
    def CreateDocumentList(cant_result):
        '''
        Clase que crea una lista con objetos Documento a partir de los archivos que recupero el crawler
        :cant_result: cantidad de documentos a procesar, solo para las pruebas
        :return: Lista con objetos de tipo Documento
        '''

        id = 0
        document_list = []
        for document in os.listdir('docs'):
            if id == cant_result:
                break
            soup = BeautifulSoup(open('docs/' + document), "lxml")
            description = ""
            for meta in soup.head.find_all('meta'):
                if 'name' in meta.attrs and 'content' in meta.attrs and meta.attrs['name'] == "description":
                    description = meta.attrs['content']

            document_tmp = Documento(id, str(document).replace('|', '/'), soup.title.string if soup.title else '',
                                     description)
            document_list.append(document_tmp)
            id += 1

        return document_list

# Pruebas
# def Test():
#   list = Controller.GenerateIndex()
# Test()
