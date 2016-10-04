from spimiProcess import SPIMI

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