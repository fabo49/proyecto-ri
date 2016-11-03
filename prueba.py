from spimiProcess import SPIMI
from LanguageProcessing import *
from time import time
def Experiment(postings, stop_words):
    block = postings
    file_name = 0
    max_mem = 1400
    start_time = time()
    while len(block) != 0:
        try:
            if len(block) < max_mem:
                leng = len(block)
            else:
                leng = max_mem
            SPIMI([block.pop(0) for x in xrange(leng)], file_name)
        except IndexError as ie:
            pass
        file_name += 1
    tiempo_sin_stop_words = time() - start_time
    print "\n- Tardo " + str(tiempo_sin_stop_words) + " segundos haciendo el indice sin stop words\n" if stop_words else "- Tardo " + str(tiempo_sin_stop_words) + " segundos haciendo el indice con stop words\n"

def Test():
    clean_file = LanguageProcessing.CleanHTML('reactive.html')
    tokens_1_ssw = LanguageProcessing.Tokenize(clean_file, True)	# Tokeniza un archivo sin stop words
    tokens_1_csw = LanguageProcessing.Tokenize(clean_file, False)	# Tokeniza un archivo con stop words
    clean_file = LanguageProcessing.CleanHTML('prueba.html')
    tokens_2_ssw = LanguageProcessing.Tokenize(clean_file, True)	# Tokeniza otro archivo sin stop words
    tokens_2_csw = LanguageProcessing.Tokenize(clean_file, False)	# Tokeniza otro archivo sin stop words
    postings = []
    postings_2 = []
    for token in tokens_1_ssw:
        print "%s" %token
        postings.append((token, 1))

    for token in tokens_2_ssw:        
        print "%s" %token
        postings_2.append((token, 2))
        
    postings_sw = postings + postings_2
    Experiment(postings_sw, True)
    postings = []
    postings_2 = []
    for token in tokens_1_csw:
        postings.append((token, 1))

    for token in tokens_2_csw:
        postings_2.append((token, 2))
        postings_2.append((token, 2))

    postings_csw = postings + postings_2
    Experiment(postings_csw, False)


Test()
"""
def main():
	tokens = [('after',1),('investigating',2),('the',3),('plantation',0),('for',1),('fair',2),('farming',3),('and',4),('climate',1),('and',2),('environmentally',0),('friendly',3),('production',1),('methods',1),('the',0),('organization',2),('the',1),('rank',4),('a',0),('rand',2),('has',3),('rated',1),('the',2),('costa',3),('rican',3),('banana',4)]
	block = []
	doc_Act = 0
	for token in tokens:
		block.append(token)
	file_name = 0
	max_Mem = 10
	while len(block)!=0:
		try:
			if len(block) < 10: leng = len(block)
			else: leng = max_Mem
			SPIMI([block.pop() for x in xrange(leng)], file_name)
		except IndexError as ie:
			pass
		file_name += 1
main()
"""