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
    def CreateDocumentList():
        '''
        Clase que crea una lista con objetos Documento a partir de los archivos que recupero el crawler
        :return: Lista con objetos de tipo Documento
        '''

        id = 0
        document_list = []
        for document in os.listdir('docs'):
            soup = BeautifulSoup(open('docs/' + document), "lxml")
            document_tmp = Documento(id, str(document).replace('|', '/'), soup.title.string if soup.title else '')
            document_list.append(document_tmp)
            id += 1

        return document_list


# Pruebas
#def Test():
#   list = Controller.GenerateIndex()
#Test()
