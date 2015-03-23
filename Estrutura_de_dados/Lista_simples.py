from os import system

cod =[]
banda = []
ano = []
cd = []

def inserir():

	n_cod = input("Insira o código: ")
	n_banda = input("insira a banda: ")
	n_cd = input("insira o cd: ")
	n_ano = input("insira o ano: ")

	cod.append(n_cod)
	banda.append(n_banda)
	cd.append(n_cd)
	ano.append(n_cd)

	input("\n\nDigite enter para continuar")

def buscar():
	if cod == []:
		print("Lista vazia")

	else:
		n_cod = input("Insira o código: ")

		print(banda[cod.index(n_cod)],cd[cod.index(n_cod)],ano[cod.index(n_cod)])
		
	input("\n\nDigite enter para continuar")

def remover():

	if cod == []:
		print("Lista vazia")

	else:	
		n_cod = input("Insira o código: ")

		del(cod[n_cod])
		del(banda[n_cod])
		del(cd[n_cod])
		del(ano[n_cod])

	input("\n\nDigite enter para continuar")

def imprimir():

	if cod == []:
		print("Lista vazia")
	else:
		for c in range(len(cod)):
			print(cod[c],banda[c],cd[c],ano[c])

	input("\n\nDigite enter para continuar")

def menu():

	system("clear")
	print("1. Inserir")
	print("2. Imprimir")
	print("3. Buscar")
	print("4. Remover")
	print("5. Sair")

	opt = input("Digite a opção desejada: ")

	if opt is "1":
		inserir()
	elif opt is "2":
		imprimir()
	elif opt is "3":
		buscar()
	elif opt is "4":
		remover()
	else:
		exit()

def main():
	while True:
		menu()

main()
