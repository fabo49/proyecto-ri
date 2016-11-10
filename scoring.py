'''
Universidad de Costa Rica
Escuela de Ciencias de la Computacion e Informatica
CI-2414: Recuperacion de la informacion
Tarea programada 1
@author: Brayan Salas B26050
@author: Fabian Rodriguez B25695
'''
from LanguageProcessing import *
from HelpMethods import *
import os
from math import *


class Scoring(object):
    @staticmethod
    def Score(query, ind, dic, mode):
        if mode: print "[debug]: Buscando: \"%s\"" % query

        index_file = open(ind, "r")
        index = HelpMethods.FileToList(index_file)
        index_file.close()
        dictionary_file = open(dic, "r")
        dictionary = HelpMethods.FileToDictionary(dictionary_file)
        dictionary_file.close()

        # Manejo de los cambios de linea
        for i in index:
            pos = index.index(i)
            index[pos] = index[pos].split()[0]

        for key, value in dictionary.items():
            value[-1] = value[-1].split()[0]

        query_tokenize = LanguageProcessing.Tokenize(query, True)
        query_terms = []
        docsResult = []
        list_docs = []

        # Variables de calculo tf-idf
        N = len(os.listdir("docs"))  # Cantidad de documentos en el sistema
        tf = []  # tf unweighted
        tf_w = []  # tf weighted
        df = []  # df
        idf = []  # idf
        tf_idf = []  # tf-idf
        neclui = []  # Normalizacion euclideana
        lnorm = []  # Length normalization

        # Se buscan las listas de postings de los distintos terminos.
        for term in query_tokenize:
            if term in index:
                query_terms.append(dictionary[term])
                list_docs.append(dictionary[term])
                df.append(len(dictionary[term]))
            else:
                if mode: print "[debug]: Termino << %s >> no encontrado" % term
                list_docs.append(['0:0'])
                df.append(0)

        # Caso de tener 2 o mas terminos
        if len(query_terms) >= 2:

            # Busca solo los Ids de los documentos.
            docs = []
            for pList in query_terms:
                docId = []
                for term in pList:
                    docId.append(term.split(':')[0])
                docs.extend(docId)
            if mode: print "[debug]: Posting Lists: %s" % docs

            # Documentos donde aparecen al menos 2 terminos.
            x = 0
            while x < len(docs):
                doc = docs.pop(0)
                if doc in docs:
                    if doc not in docsResult:
                        docsResult.append(doc)
                x += 1
            if mode: print "[debug]: Documentos: %s" % docsResult

            N = N - len(docsResult)

        else:
        	if len(query_terms) == 1:
        		for value in query_terms[0]:
	                    docsResult.append(value.split(':')[0])
	                N = N - len(docsResult)
	                if mode: print "[debug]: Solo un termino valido: %s" % docsResult
        	else:
	            # Es solo un termino de busqueda, devuelve todos los docs.
	            if query_tokenize[0] in index:
	                for value in dictionary[query_tokenize[0]]:
	                    docsResult.append(value.split(':')[0])
	                N = N - len(docsResult)
	                if mode: print "[debug]: Documentos: %s" % docsResult

	                # Resultados Ranking
	                list_docs.append(dictionary[query_tokenize[0]])
	                df.append(len(dictionary[query_tokenize[0]]))
	            else:
	                if mode: print "[debug]: Termino '%s' no encontrado" % query_tokenize[0]
	                docsResult = []

	    if docsResult:
	        # Genera el vector de documentos para realizar tf-idf
	        for doc in docsResult:
	            freq = []
	            for query in list_docs:
	                n = 0
	                for term in query:
	                    if term.split(':')[0] == doc:
	                        freq.append(int(term.split(':')[1]))
	                        break
	                    else:
	                        if n == len(query) - 1:
	                            freq.append(0)
	                    n += 1

	            # print "frecuencia de cada term en doc: %s" %freq
	            tf.append(freq)
	        if mode: print "[debug]: TF unweighted: %s" % tf

	        # Calcula el tf de peso de cada termino en su doc
	        for tf_term in tf:
	            tFreq_w = []
	            for tfreq in tf_term:
	                if 0 < tfreq:
	                    tFreq_w.append(1 + log10(int(tfreq)))
	                else:
	                    tFreq_w.append(0)
	            tf_w.append(tFreq_w)
	        if mode: print "[debug]: TF weighted: %s" % tf_w

	        # Calculo del idf para uso
	        for dFreq in df:
	            if dFreq is not 0:
	                idf.append(log10(float(N) / float(dFreq)))
	            else:
	                idf.append(0)
	        if mode: print "[debug]: IDF: %s" % idf

	        # Calculo del peso real tf-idf
	        for tfw in tf_w:
	            tfidf = []
	            x = 0
	            for tfreq in tfw:
	                if tfreq is not 0:
	                    tfidf.append(tfreq * idf[x])
	                else:
	                    tfidf.append(0)
	                x += 1
	            tf_idf.append(tfidf)
	        if mode: print "[debug]: TF-IDF: %s" % tf_idf

	        # Calculo de la normalizacion euclideana
	        for wei_doc in tf_idf:
	            euc = 0
	            for weig in wei_doc:
	                euc += pow(weig, 2)
	            neclui.append(sqrt(euc))
	        if mode: print "[debug]: Normalizacion Euclideana: %s" % neclui

	        # Calculo de length normalization
	        x = 0
	        for tidf in tf_idf:
	            tflnor = []
	            for val in tidf:
	                if val is not 0:
	                    tflnor.append(val / neclui[x])
	                else:
	                    tflnor.append(0)
	            x += 1
	            lnorm.append(tflnor)
	        if mode: print "[debug]: Normalizacion tamano: %s" % lnorm

	        # Normalizacion de la consulta
	        query_normali = []
	        query_neucl = 0
	        lis1 = []  # Contabilizacion
	        for q in query_tokenize:
	            lis1.append(1)
	        query_normali.append(lis1)
	        lis2 = []  # tf weighted
	        for q in query_normali[0]:
	            if q is not 0:
	                lis2.append(1 + log10(q))
	            else:
	                lis2.append(0)
	        query_normali.append(lis2)
	        lis3 = []  # tf-idf
	        x = 0
	        for q in query_normali[1]:
	            lis3.append(q * idf[x])
	            x += 1
	        query_normali.append(lis3)
	        if mode: print "[debug]: Consulta [[Cant],[TF w],[TF_IDF]]: %s" % query_normali

	        for x in query_normali[1]:
	            euc += pow(x, 2)
	        query_neucl = sqrt(euc)
	        if mode: print "[debug]: Normalizacion Euclideana de consulta: %s" % query_neucl

	        query_norm = []
	        for x in query_normali[2]:
	            query_norm.append(x / query_neucl)
	        if mode: print "[debug]: Normalizacion tamano de consulta: %s" % query_norm

	        # Busqueda de resultados en comparaciones. RANKING.
	        query_vs_docs = []
	        for l in lnorm:
	            res = 0
	            for x in xrange(len(query_tokenize)):
	                res += l[x] * query_norm[x]
	            query_vs_docs.append(res)
	        if mode: print "[debug]: Similitud consulta con cada doc: %s" % query_vs_docs

	        finalResult = []
	        for x in xrange(len(docsResult)):
	            finalResult.append((docsResult[x], query_vs_docs[x]))
	        if mode: print "[debug]: Documento y su relevancia: %s" % finalResult

	        resultsPair = sorted(finalResult, key=lambda x: float(x[1]), reverse=True)

	        # if mode: print "[debug]: Resultados con ranking: %s" %results
	        if mode: print "[debug]: Resultados con ranking: %s" % resultsPair
	        results = []
	        for doc in resultsPair:
	            results.append(doc[0])

	    else:
	    	results = []

        # print "Resultados: %s" %results
        return results


        # def Test():
        #	query = "wild cats and dogs"
        #	Scoring.Score(query,'index1.txt','dict1.txt',False)
        # query = "cats"
        # Scoring.Score(query,'index1.txt','dict1.txt',True)
        # query = "dogs"
        # Scoring.Score(query,'index1.txt','dict1.txt',True)
        # query = "wild bulls and dogs educated"
        # Scoring.Score(query,'index1.txt','dict1.txt',False)

        # Test()
