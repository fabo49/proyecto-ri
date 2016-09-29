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

# ===================================================
#       Clase del procesamiento linguistico
# ===================================================

class LanguageProcessing(object):
    """Clase que contiene los metodos necesarios para realizar el procesamiento linguistico de documentos"""

    @staticmethod
    def Porter(path):
        """
        Metodo estatico que se encarga de normalizar y parsear un documento con el algoritmo de Porter
            * Recibe como parametro la ruta del documento que va a parsear
        """
        porter_stemmer = PorterStemmer()
        doc = open(path, 'r')
        result = open('p_'+path, 'a')   # TODO: ELIMINAR
        # result = '' # TODO: descomentar
        for line in doc:
            for word in line.split(' '):    # Se ocupa usar split(' ') para que solo haga split por espacios, si se usa split() tambien cuenta los cambios de linea
                # result += porter.stem(word).lower() if word.endswith('\n') else porter.stem(word).lower() + ' ' # TODO: descomentar
                result.write(porter_stemmer.stem(word).lower()) if word.endswith('\n') else result.write(porter_stemmer.stem(word).lower()+' ')     # TODO: ELIMINAR
        doc.close()
        result.close()
        # result # TODO: descomentar

LanguageProcessing.Porter('prueba.txt')