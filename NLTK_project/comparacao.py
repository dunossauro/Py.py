def compare():
	wl1 = input("Digite o nome da WordList 1: ")
	wl2 = input("Digite o nome da WordList 2: ")

	arq_1 = open(wl1)
	arq_2 = open(wl2)

	D1 = {}
	for x in arq_1:
		num, word = x.split()
		D1[word] = num

	D2 = {}
	for x in arq_2:
		num, word = x.split()
		D2[word] = num

	nome_s = input("Digite o nome do arquivo que deseja gravar a saída: ")

	arquivo_s = open(nome_s,"w")
	
	for x in sorted(D1):
		for y in D2:
			if x == y:
				arquivo_s.write(("%s\t%s\t%s\t%s\n")%(D1[x],x,y,D2[y]))

	arquivo_s.close()
