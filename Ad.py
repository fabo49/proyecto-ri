'''
Universidad de Costa Rica
Escuela de Ciencias de la Computacion e Informatica
CI-2414: Recuperacion de la informacion
Proyecto programado
@author: Brayan Salas B26050
@author: Fabian Rodriguez B25695
'''

from datetime import datetime
from LanguageProcessing import *
import os


class Ad(object):
    '''
    Modelo de la entidad Anuncio que posee los siguientes atributos:
        * id: identificador unico del anuncio
        * title: titulo del anuncio
        * description: descripcion del anuncio
        * link: enlace a la pagina del anunciante
        * keywords: una lista con las palabras claves para ligar el anuncio con una consulta
        * cant_visits: el numero de visitas por el que pago el usuario para que el anuncio sea mostrado
    '''

    def __init__(self, title="", description="", link="", keywords="", cant_visits=""):
        '''
        Constructor de la clase
        :param title: string con el titulo del anuncio
        :param description: string con la descripcion del anuncio
        :param link: string con el link a la pagina del anunciante
        :param keywords: string de las palabras claves separadas por comas (,)
        :param cant_visits: la cantidad de visitas que puede tener el anuncio
        '''
        self.title = title
        self.description = description
        self.link = link
        self.keywords = []
        keywords_tmp = keywords.split(',')
        for keyword in keywords_tmp:
            self.keywords.extend(LanguageProcessing.Tokenize(keyword, True))
        self.keywords.extend(LanguageProcessing.Tokenize(self.title, True))
        self.keywords = list(set(self.keywords))
        self.id = datetime.now()
        self.cant_visits = cant_visits

    def SaveAd(self):
        '''
        Metodo que guarda un registro de un ad en el archivo ads.txt
        '''
        line = str(self.id) + '|' + self.title + '|' + self.link + '|' + self.description + '|' + self.cant_visits + '|'
        for keyword in self.keywords:
            line += keyword + ','
        line = line[:-1]  # Quito la coma adicional
        ads_file = open('ads.txt', 'a')
        ads_file.write(line)
        ads_file.write('\n')
        ads_file.close()

    def UpdateAd(self):
        '''
        Metodo que resta una visita de total que tiene el anuncio y actualiza el archivo ads.txt
        :return:
        '''
        ads = Ad.Ads()
        Ad.ClearAds()
        for ad in ads:
            if ad.id == self.id:
                ad.cant_visits = str(int(ad.cant_visits) - 1)
            ad.SaveAd()

    @staticmethod
    def GetAd(link):
        '''
        Metodo que busca un anuncio con base en el link que recibe
        :param link: link que desea buscar a cual anuncio le pertenece
        :return: Objeto tipo Ad que corresponde al anuncio con el link que recibe de parametro, si no lo encuenta retorna un objeto Ad vacio
        '''
        ads = Ad.Ads()
        found = False
        index = 0
        while index < len(ads) and not found:
            if ads[index].link == link:
                found = True
            else:
                index += 1
        return ads[index] if found else Ad()

    @staticmethod
    def Ads():
        '''
        Metodo que lee del archivo ads.txt y retorna una lista con todos los anuncios
        :return: lista con todos los anuncios
        '''
        ads_list = []
        ads_file = open('ads.txt', 'r')
        for ad in ads_file:
            if ad != '\n':
                saved_ad = ad.split('|')
                ad_tmp = Ad()
                ad_tmp.id = saved_ad[0]
                ad_tmp.title = saved_ad[1]
                ad_tmp.link = saved_ad[2]
                ad_tmp.description = saved_ad[3]
                ad_tmp.cant_visits = saved_ad[4]
                ad_tmp.keywords = saved_ad[5].split(',')
                ads_list.append(ad_tmp)
        ads_file.close()
        return ads_list

    @staticmethod
    def ClearAds():
        '''
        Metodo que elimina todos los registros de anuncios
        '''
        if os.path.isfile('ads.txt'): os.remove('ads.txt')

        # def Test():

    #    Ad.ClearAds()

    #    ad1 = Ad('Titulo 1', 'Una descripcion bonita', 'http://google.com', 'perro,gato,animales', '30')
    #    ad2 = Ad('Titulo 2', 'Una descripcion bonita', 'http://google.com', 'perro,gato,animales', '30')
    #    ad3 = Ad('Titulo 3', 'Una descripcion bonita', 'http://google.com', 'perro,gato,animales', '30')

# ad4 = Ad('Toptal','Toptal is a marketplace for top developers, engineers, programmers, and consultants. Top companies and start-ups hire freelance developers from Toptal for their most mission-critical projects.','https://www.toptal.com/developers', 'computers,science,jobs,toptal', '200')
#    ad4.SaveAd()


#    ads = Ad.Ads()


# Test()
