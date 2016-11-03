'''
Universidad de Costa Rica
Escuela de Ciencias de la Computacion e Informatica
CI-2414: Recuperacion de la informacion
Tarea programada 1
@author: Brayan Salas B26050
@author: Fabian Rodriguez B25695
'''

def score(query,ind,dic):
	index = open(ind, "r")
	dictionary = open(dic, "r")
	query_terms = {}
	terms_readed = []

	act_term = index.readLine()
	terms_readed.append(act_term)
	for term in query:
		if term in terms_readed:
			l = getPostingList(term)
			query_terms.append(l)
		else:
			while act_term not term and act_term not "":
				act_term = index.readLine()
				terms_readed.append(act_term)
			if act_term is term:
				l = getPostingList(term)
				query_terms.append(l)
			else:
				if act_term not term and act_term is "":
					print "Termino no encontrado"