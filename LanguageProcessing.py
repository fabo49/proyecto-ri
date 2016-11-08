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

from nltk.stem.porter import *  # Modulo con el algoritmo de Porter para hacer stemming
from stop_words import get_stop_words  # Modulo con stop_words en distintos idiomas
from bs4 import BeautifulSoup  # Para parsear documentos HTML


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
    def Porter(tokens_list):
        """
        Metodo estatico que se encarga hacer stemming a un documento con el algoritmo de Porter
        :param document: Una lista de tokens a los que se les queire hacer stemming.
        :return: Una lista con los tokens ya pasados por el algoritmo de Porter
        """
        porter_stemmer = PorterStemmer()
        result = []
        for token in tokens_list:
            result.append(porter_stemmer.stem(token))
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
        clean_file = BeautifulSoup(open(path), "lxml")
        for script in clean_file.find_all('script'):
            script.extract()
        return clean_file.get_text()

    @staticmethod
    def CleanToken(token):
        '''
        Metodo que elimina caracteres indeseados en los tokens como puntos, comas, comillas, dos puntos, punto y coma, comillas dobles, etc...
        :param token:
        :return:
        '''
        return token.lower().replace(',', '').replace('.', '').replace('\'', '').replace(':', '').replace(';',
                                                                                                          '').replace(
            '\"',
            '').replace('(', '').replace(')', '').replace('!', '').replace('?', '')

    @staticmethod
    def Tokenize(file, eliminate_stop_words):
        """
        Metodo que se encarga de normalizar el documento (pasando a lowercase) y elimina las stop_words si el usuario lo pide.
        :param file: String con el archivo que se va a tokenizar.
        :param eliminate_stop_words: Booleano que indica si se eliminan los stop_words.
        :return: Una lista con los tokens del archivo
        """
        result = []
        tokens = file.split()
        for token in tokens:
            if token not in result:
                result.append(
                    '' if eliminate_stop_words and LanguageProcessing.IsStopWord(
                        LanguageProcessing.CleanToken(token)) else LanguageProcessing.CleanToken(token))
        return LanguageProcessing.Porter(
            filter(None, result))  # Elimina los campos vacios de la lista y se aplica el algoritmo de Porter

        # ===================
        #       Pruebas
        # ===================
        # def Test():
        #    clean_file = LanguageProcessing.CleanHTML("reactive.html")  # Se eliminan los tags de html del archivo para extraer el texto
        #    print clean_file
        #    tokens = LanguageProcessing.Tokenize(clean_file, True)      # Se hace la lista de tokens SIN stop words y se aplica el algoritmo de Porter para stemming de los tokens
        #    a = 1
        #    print "\nHay "+str(len(tokens))+" tokens en la lista sin stop words.\n"
        #    tokens = LanguageProcessing.Tokenize(clean_file, False)     # Se hace la lista de tokens CON stop words y se aplica el algoritmo de Porter para stemming de los tokens
        #    print "Hay "+str(len(tokens))+" tokens en la lista con stop words.\n"

        # Test()  # Se ejecutan las pruebas
