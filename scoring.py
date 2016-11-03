'''
Universidad de Costa Rica
Escuela de Ciencias de la Computacion e Informatica
CI-2414: Recuperacion de la informacion
Tarea programada 1
@author: Brayan Salas B26050
@author: Fabian Rodriguez B25695
'''
from LanguageProcessing import tokenize
from helpers import FileToList, FileToDictionary

def score(query,ind,dic):
	index_file = open(ind, "r")
	index = FileToList(index_file)
	index_file.close()
	dictionary_file = open(dic, "r")
	dictionary = FileToDictionary(dictionary_file)
	dictionary_file.close()

	query_tokenize = tokenize(query)
	query_terms = []

	# Se buscan las listas de postings de los distintos terminos.
	for term in query_tokenize:
		if term in index:
			query_terms.append(dictionary[term])
		else:
			print "[debug]: Termino no encontrado"

	# Se encuentra el posting_list de menor tamaño
	posAct = 0
	posListThin = 0
	listThin = len(query_terms[0])
	for posting_list in query_terms:
		if len(posting_list) < listThin:
			posListThin = posAct
			listThin = len(posting_list)
			posAct += 1
		else:
			posAct += 1

	# Se busca en cuales documentos se encuentran estos terminos.
	postingListThin = query_terms.pop(posListThin)
	docsAppears = []
	for x in xrange(listThin):
		for lis in query_terms:
			while 0 < len(lis) and lis[0].split(':')[0] < postingListThin[x].split(':')[0]:
				lis.pop(0)
			if len(lis) is not 0 and lis[0].split(':')[0] = postingListThin[x].split(':')[0]:
				if lis[0] not in docsAppears:
					docsAppears.append(lis[0])
	