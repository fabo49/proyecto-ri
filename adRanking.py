'''
Universidad de Costa Rica
Escuela de Ciencias de la Computacion e Informatica
CI-2414: Recuperacion de la informacion
Tarea programada 1
@author: Brayan Salas B26050
@author: Fabian Rodriguez B25695
'''
import os
from Ad import *
from LanguageProcessing import *


class adRanking(object):
    '''
        Clase que toma el query y busca los anuncios que contienen esos keywords
    '''

    @staticmethod
    def ranking(query):
        ad_list = Ad.Ads()  # Obtiene los ads en una lista
        query_tokenize = LanguageProcessing.Tokenize(query, True)  # Obtiene la query tokenizada
        # print query_tokenize

        ad_results = []
        freq_ad_results = []
        for ad_i in ad_list:
            for keyword in ad_i.keywords:
                if keyword.split()[0] in query_tokenize:    # si el keyword es parte de la busqueda
                    if ad_i.link in ad_results:             # si el ad ya se encontraba aumente cont
                        pos = ad_results.index(ad_i.link)
                        freq_ad_results[pos] = freq_ad_results[pos] + 1
                    else:
                        ad_results.append(ad_i.link)        # se agrega si el ad no estaba incluido
                        freq_ad_results.append(1)           # se indica que ha aparecido una vez
                        
        
        # print ad_results
        # print freq_ad_results
        
        ranked_results = []
        max_freq = 0
        while True:
            # busca cual es la frecuencia mayor
            for x in freq_ad_results:
                if max_freq < x:
                    max_freq = x

            # agrega los ads con la freq encontrada
            y = 0
            while y < len(ad_results):
                if max_freq == freq_ad_results[y]:
                    ranked_results.append(ad_results[y])
                    ad_results.pop(y)
                    freq_ad_results.pop(y)
                y += 1

            max_freq = 0

            if not ad_results:
                break

        # print "llega aqui"

        results = []
        for res in ranked_results:
            results.append(Ad.GetAd(res))

        return list(set(results))

        # def Test():
        #    res = adRanking.ranking("photography")
        #    print res[0].title

        # Test()
