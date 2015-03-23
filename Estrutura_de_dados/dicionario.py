from os import system

lista = {}

def inserir():

	cod = input("Insira o código: ")
	nome = input("insira o Nome: ")

	lista[cod] = nome

	input("\n\nDigite enter para continuar")

def buscar():
	if lista == {}:
		print(lista)

	else:
		cod = input("Insira o código: ")

		print(lista[cod])
		
	input("\n\nDigite enter para continuar")

def remover():

	if lista == {}:
		print(lista)
	else:	
		cod = input("Insira o código: ")

		print(lista[cod], "Foi removido")

		del(lista[cod])

	input("\n\nDigite enter para continuar")

def imprimir():

	print(lista)

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
