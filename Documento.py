'''
Universidad de Costa Rica
Escuela de Ciencias de la Computacion e Informatica
CI-2414: Recuperacion de la informacion
Tarea programada 1
@author: Brayan Salas B26050
@author: Fabian Rodriguez B25695
'''

class Documento(object):
    '''
    Clase que se utiliza para crear objetos tipo Documento con los siguientes atributos:
        * id: identificador unico
        * url: url del documento
        * title: titulo de la pagina del documento
    '''

    def __init__(self, id="", url="", title=""):
        '''
        Constructor de la clase.
        '''
        self.id = id
        self.url = url
        self.title = title

    # Getters
    def GetId(self):
        return self.id

    def GetUrl(self):
        return self.url

    def GetTitle(self):
        return self.title

    # Setters
    def SetId(self, new_id):
        self.id = new_id

    def SetUrl(self, new_url):
        self.url = new_url

    def SetTitle(self, new_title):
        self.title = new_title

    def PrintResult(self):
        '''
        Metodo que imprime la informacion del objeto documento para control.
        :return: Imprime los atributos del resultado.
        '''
        print "-- [DEBUG] --"
        print "Datos del resultado:"
        print "  * Identificador: " + str(self.id)
        print "  * Titulo: " + self.title
        print "  * URL: " + self.url

# Pruebas
#result = Resultado(1, "https://aecci.ecci.ucr.ac.cr", "AECCI | UCR")
#result.PrintResult()
#print "\nActualizamos datos...\n"
#result.SetTitle("Pagina de la asociacion de estudiantes de la ECCI")
#result.PrintResult()

#print "\nSegundo objeto\n"
#result2 = Resultado(2, "http://google.com")
#result2.PrintResult()
