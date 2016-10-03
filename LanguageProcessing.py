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
import re       # Para eliminar los tags de html del texto

# ===================================================
#       Clase del procesamiento linguistico
# ===================================================

class LanguageProcessing(object):
    """
    Clase que contiene los metodos necesarios para realizar el procesamiento linguistico de documentos.

    Requiere que los modulos nltk y stop-words esten instalados, para instalarlos ingrese los siguientes comandos en
    la terminal:
        * sudo pip install stop-words
        * sudo pip install -U nltk
    """

    @staticmethod
    def Porter(path):
        """
        Metodo estatico que se encarga de normalizar y parsear un documento con el algoritmo de Porter
        :param path: La ruta del documento a parsear
        :return: Un archivo en la misma ruta y con el mismo nombre pero con el prefijo 'p_' donde esta el documento parseado con Porter
        """
        porter_stemmer = PorterStemmer()
        doc = open(path, 'r')
        result = open('p_'+path, 'a')
        for line in doc:
            for word in line.split(' '):    # Se ocupa usar split(' ') para que solo haga split por espacios, si se usa split() tambien cuenta los cambios de linea
                result.write(porter_stemmer.stem(word).lower()) if word.endswith('\n') else result.write(porter_stemmer.stem(word).lower()+' ')
        doc.close()
        result.close()

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
        :return: Un archivo con los tags eliminados.
        """
        doc = open(path, 'r')
        result = open('c_'+path+'.txt','a')
        cleaner = re.compile('<.*?>')
        for line in doc:
            result.write(re.sub(cleaner,'', line))
        doc.close()
        result.close()

# ===================
#       Pruebas
# ===================
# LanguageProcessing.Porter('prueba.txt')
# print 'Hola' if LanguageProcessing.IsStopWord('a') else 'Adios'
LanguageProcessing.CleanHTML('index.html')