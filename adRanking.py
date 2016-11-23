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
        ad_list = Ad.Ads()   # Obtiene los ads en una lista
        query_tokenize = LanguageProcessing.Tokenize(query, True)   # Obtiene la query tokenizada
        
        ad_results = []
        freq_ad_results = []
        for ad_i in ad_list:
            for keyword in ad_i.keywords:
                if keyword in query_tokenize:
                    if ad_i.link in ad_results:
                        pos = ad_results.index(ad_i.link)
                        freq_ad_results[pos] = freq_ad_results[pos] + 1
                    else:
                        ad_results.append(ad_i.link)
                        freq_ad_results.append(1)
                
        ranked_results = []
        max_freq = 0
        tam = len(ad_results)
        while True:
            for x in freq_ad_results:
                if max_freq < x:
                    max_freq = x
                    
            for y in xrange(len(ad_results)):
                if max_freq == freq_ad_results[y]:
                    ranked_results.append(ad_results[y])
                    print ranked_results[-1]
                    ad_results.pop(y)
                    print ranked_results[-1]
                    
            max_freq = 0
            
            if not ad_results:
                break
                        
        results = []
        for res in ranked_results:
            results.append(Ad.GetAd(res))
            
        return results