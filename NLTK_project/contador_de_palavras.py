#V: 0.0.2

from nltk import Text,FreqDist,word_tokenize

def plot(token, num=10):

	texto = Text(token)

	texto.plot(num)

def contagem():

	#Entrada
	nome_e = input("Digite o nome do arquivo que deseja contar palavras: ")
	nome_s = input("Digite o nome do arquivo que deseja gravar a saída: ")

	#Abertura do aquivo a ser lido
	arquivo_e = open(nome_e).read()

	#Abertura do arquivo de saida
	arquivo_s = open(nome_s,"w")

	#tokenização do arquivo
	token = word_tokenize(arquivo_e)

	#Análise de frequência
	num = FreqDist(token)

	#Exibição da contagem
	num = num.most_common(len(num))
	
	for x,y in num:
		arquivo_s.write(("%s\t\t%s\n")%(y,x))

	arquivo_s.close()

	graf = input("Deseja exibir o gráfico das palavras mais frequentes? S/N: ")

	if graf == 's' or graf == 'S':

		plot(token)
