from spimiProcess import SPIMI

def main():
	tokens = ['manzana','banano','uva','uva','uva','manzana','limon','limon','melocoton','papaya','banano']
	block = []
	doc_Act = 0

	for token in tokens:
		doc_Act += 1
		doc_id = doc_Act%3
		pair = (token,doc_id)
		block.append(pair)

	SPIMI(block)

main()