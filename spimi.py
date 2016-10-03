'''
Universidad de Costa Rica
Escuela de Ciencias de la Computacion e Informatica
CI-2414: Recuperacion de la informacion
Tarea programada 1
@author: Brayan Salas B26050
@author: Fabian Rodriguez B25695
'''

class SPIMI(token_stream):
	# Se utiliza open para crear el archivo donde va a estar el output_file
	with open("output_spimi.txt","wb") as output_file:
		dictionary = {}
		for token in token_stream:
			# pair[0] => token, pair[1] => doc_id
			pair = [toke[0],token[1]]
			if pair[0] is not dictionary:
				posting_list = add_to_dictionary(dictionary,pair[0])
			else:
				posting_list = get_posting_list(dictionary,pair[0])
			add_to_dictionary(posting_list,pair[1])

def add_to_dictionary(dictionary, term):
	dictionary[term] = []
	return dictionary[term]

def get_postings_list(dictionary, term): 
	return dictionary[term]	

def add_to_postings_list(postings_list, doc_id): 
	if doc_id not in postings_list:
		postings_list.insert(0,doc_id)
	else: 
		postings_list