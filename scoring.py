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

	query_terms = tokenize(query)

# Rediseñar desde aquí
	act_term = index.readLine()
	terms_readed.append(act_term)
	for term in query:
		if term in terms_readed:
			l = getPostingList(term,dictionary)
			query_terms.append(l)
		else:
			while act_term not term and act_term not "":
				act_term = index.readLine()
				terms_readed.append(act_term)
			if act_term is term:
				l = getPostingList(term,dictionary)
				query_terms.append(l)
			else:
				if act_term not term and act_term is "":
					print "Termino no encontrado"
# Hasta aquí

	# Se encuentra el posting_list de menor tamaño
	posAct = 0
	posListThin = 0
	listThin = len(query_terms[0])
	for posting_list in query_terms:
		if listThin < len(posting_list):
			posListThin = posAct
			listThin = len(posting_list)
		else:
			posAct += 1

	# Se busca en cuales documentos se encuentran estos terminos.
	postingListThin = query_terms.pop(posListThin)
	docsAppears = []
	for x in xrange(listThin):
		for lis in query_terms:
			while 0 < len(lis) and lis[0] < postingListThin[x]:
				lis.pop(0)
			if len(lis) is not 0 and lis[0] = postingListThin[x]:
				if lis[0] not in docsAppears:
					docsAppears.append(lis[0])

# Busca en el diccionario el postings_list del termino.
def getPostingList(term,dic):
	