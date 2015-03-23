print("Esse programa executa o calculo de Drake para descobrir o número(probabilístico) para estimar o  número de civilizações extraterrestres\
	com as quais podemos estabelecer comunicação\n")

print("Números reais: \n\
	\n\
	R*, Taixa de formação de estrelas em nossa galáxia: 																				7/ano\n\
	fp, Fração de estrelas que possuem planetas em órbita: 																				0,5\n\
	ne, Número médio de planetas que potencialmente permitem o desenvolvimento de vida por estrelas que tem planetas:					2\n\
	fl, Fração dos planetas com potencial para vida que realmente desenvolvem vida:														0,33\n\
	fi, Fração de potencial que desenvolvem vida inteligente:																			0,01\n\
	fc, Fração de planetas que desenvolvem vida inteligente e que têm o desejo e os meios necessários para estabelecer comunicação: 	0,01\n\
	L,  Tempo esperado de vida de tal civilização: 																						10 000 anos\n\
	\n\
O objetivo do programa é podermos imaginar vida extraterrestres em outras galáxias, ou imaginar outros valores.\
	")


R = float(input("Insira a taixa de formação de estrelas em nossa galáxia:   "))
FP = float(input("Insira a fração de estrelas que possuem planetas em órbita:   "))
NE = float(input("Insira o número médio de planetas que potencialmente permitem o desenvolvimento de vida por estrelas que tem planetas:   "))
FL = float(input("Insira a fração dos planetas com potencial para vida que realmente desenvolvem vida:   "))
FI = float(input("Insira a fração de potencial que desenvolvem vida inteligente:   "))
FC = float(input("Insira a fração de planetas que desenvolvem vida inteligente e que têm o desejo e os meios necessários para estabelecer comunicação:   "))
L = float(input("Insira o tempo esperado de vida de tal civilização:   "))


N = R*FP*NE*FL*FI*FC*L

print("o número de civilizações extraterrestres em nossa galáxia com as quais poderíamos ter chances de estabelecer comunicação é: ", N)
