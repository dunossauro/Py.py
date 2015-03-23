from os import system

lista = []

def inserir():

	cod = input("Insira o código: ")
	banda = input("insira a banda: ")
	cd = input("insira o cd: ")
	ano = input("insira o ano: ")

	lista.append([cod,banda,cd,ano])

	input("\n\nDigite enter para continuar")

#FAZER
def buscar():
	if lista == []:
		print("Lista vazia")

	else:
		cod = input("Insira o código: ")
		
	input("\n\nDigite enter para continuar")

#FAZER
def remover():

	if cod == []:
		print("Lista vazia")

	else:	

	input("\n\nDigite enter para continuar")

def imprimir():

	if lista == []:
		print("Lista vazia")
	else:
		for x in lista:
			print(x)

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
