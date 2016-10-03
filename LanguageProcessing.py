'''
Universidad de Costa Rica
Escuela de Ciencias de la Computacion e Informatica
CI-2414: Recuperacion de la informacion
Tarea programada 1
@author: Brayan Salas B26050
@author: Fabian Rodriguez B25695
'''

# ============================
#       Modulos externos
# ============================

from nltk.stem.porter import *   # Modulo con el algoritmo de Porter para hacer stemming
from stop_words import get_stop_words   # Modulo con stop_words en distintos idiomas
from bs4 import BeautifulSoup   # Para parsear documentos HTML

# ===================================================
#       Clase del procesamiento linguistico
# ===================================================

class LanguageProcessing(object):
    """
    Clase que contiene los metodos necesarios para realizar el procesamiento linguistico de documentos.

    Requiere que los modulos nltk, BeautifulSoup y stop-words esten instalados, para instalarlos ingrese los siguientes comandos en
    la terminal:
        * sudo pip install stop-words
        * sudo pip install -U nltk
        * sudo pip install beautifulsoup4
        * sudo pip install lxml
    """

    @staticmethod
    def Porter(document):
        """
        Metodo estatico que se encarga de normalizar y hacer stemming a un documento con el algoritmo de Porter
        :param document: Un string con el archivo que desea hacerle stemming.
        :return: Una hilera con el documento parseado con Porter
        """
        porter_stemmer = PorterStemmer()
        result = ""
        words = document.split(' ')
        for word in words:
            result += porter_stemmer.stem(word).lower() if word.endswith('\n') else porter_stemmer.stem(word).lower()+' '
        return result

    @staticmethod
    def IsStopWord(word):
        """
        Metodo que revisa si una parabra esta dentro de la lista de stop words del idioma ingles.
        :param word: la palabra que se desea averiguar si es una stop word.
        :return: True si es una stop word, False en caso contrario
        """
        stop_words = get_stop_words('en')
        return word in stop_words

    @staticmethod
    def CleanHTML(path):
        """
        Metodo estatico que se encarga de eliminar todos los tags de html de un documento.
        :param path: La ruta del documento a eliminar los tags.
        :return: Una hilera que contiene el texto del archivo HTML sin tags.
        """
        return BeautifulSoup(open(path), "lxml").get_text()

    @staticmethod
    def CleanFile(file, eliminate_stop_words):
        """
        Metodo que se encarga de normalizar el documento (pasando a lowercase) y elimina las stop_words si el usuario lo pide.
        :param file: String con el archivo que se va a tokenizar.
        :param eliminate_stop_words: Booleano que indica si se eliminan los stop_words.
        :return: Una lista con los tokens del archivo
        """
        result = []
        tokens = file.split()
        for token in tokens:
            result.append(('' if LanguageProcessing.IsStopWord(token) else token.lower()) if eliminate_stop_words else token.lower())
        return result

# ===================
#       Pruebas
# ===================
# LanguageProcessing.Porter('prueba.txt')
# print 'Hola' if LanguageProcessing.IsStopWord('a') else 'Adios'
parsed = LanguageProcessing.CleanHTML('prueba.html')
print LanguageProcessing.CleanFile(parsed, True)