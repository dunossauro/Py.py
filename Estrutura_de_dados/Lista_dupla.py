###############################
# Lista duplamente encadeada #
###############################

class No:
    def __init__(self, carga=None, idade=0, proximo=None, anterior=None):
        self.nome = carga
        self.idade = idade
        self.proximo = proximo
        self.anterior = anterior

    def __str__(self):
        return (("%s\t\t%s")%(self.nome, self.idade))

#Função de impressão
def imprime_frente(no):
    print("Nome\t\tIdade")
    print("----------------------")
    while no:
        print(no)
        no = no.proximo

#Função de impressão
def imprime_verso(no):
    print("Nome\t\tIdade")
    print("----------------------")
    while no:
        print(no)
        no = no.anterior

#Atribuição dos valores aos nós
no1 = No("Eduardo", 22)
no2 = No("Ana", 35)
no3 = No("Taina", 21)
no4 = No("Wilzão", 20)

#Encadeando nós
no1.proximo = no2
no2.proximo = no3
no3.proximo = no4

no2.anterior = no1
no3.anterior = no2
no4.anterior = no3

imprime_frente(no1)
print("\n")
imprime_verso(no4)

#Circular
#no4.proximo = no1
