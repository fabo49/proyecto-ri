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


from stemming.porter2 import stem as porter     # Algoritmo Porter2 para hacer stemming
from stemming.lovins import stem as lovins      # Algoritmo Lovins para hacer stemming

# ========================
#       Clase Parser
# ========================

# Clase que contiene los metodos necesarios para parsear documentos
class Parser(object):
    '''Clase que contiene los metodos necesarios para parsear documentos'''

    def parse_porter(doc):
        '''Metodo estatico que se encarga de normalizar y parsear el documento con el algoritmo de Porter'''
        porter("hello")

    def parse_lovins(doc):
        '''Metodo estatico que se encarga de normalizar y parsear el documento segun el algorimto de Lovins'''
        lovins("goodbye")