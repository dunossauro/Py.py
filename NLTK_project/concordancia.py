import nltk, itertools

#Base to function: https://simplypython.wordpress.com/2014/03/14/saving-output-of-nltk-text-concordance/
def concordance_2_txt(nome_p, tokens, left_margin = 2, right_margin = 4):
     
    text = nltk.Text(tokens)
    c = nltk.ConcordanceIndex(text.tokens)
    
    concordance_txt = ([text.tokens[list(map(lambda x: x-5 if (x-left_margin)>0 else 0,[offset]))[0]:offset+right_margin]
                        for offset in c.offsets(nome_p)])
                         
    return [''.join([x+' ' for x in con_sub]) for con_sub in concordance_txt]


def concord():

	#Entrada
	nome_e = input("Digite o nome do arquivo que deseja encontrar concordancias: ")
	nome_p = input("Digite a palavra que deseja encontrar concordancias: ")

	#Abertura do aquivo a ser lido
	arquivo_e = open(nome_e).read()
	
	#tokenização do arquivo
	token = nltk.word_tokenize(arquivo_e)

	texto = nltk.Text(token)

	texto.concordance(nome_p)
	
	bool_ = input("Deseja salvar em um arquivo? S/N: ")

	if bool_ == 's' or bool_ == 'S':

		nome_s = input("Digite o nome do arquivo que deseja gravar a saída: ")

		#Abertura do arquivo de saida
		arquivo_s = open(nome_s,"w")

		saida = concordance_2_txt(nome_p, token)

		for x in saida:			
			arquivo_s.write(("%s\n")%(x))
		
		arquivo_s.close()
