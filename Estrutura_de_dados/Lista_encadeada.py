###############################
# Lista simplemente encadeada #
###############################

class No:
    def __init__(self, carga=None, idade=0, proximo=None):
        self.nome = carga
        self.idade = idade
        self.proximo = proximo

    def __str__(self):
        return (("%s\t\t%s")%(self.nome, self.idade))

#Função de impressão
def imprime(no):
    print("Nome\t\tIdade")
    print("----------------------")
    while no:
        print(no)
        no = no.proximo

#Atribuição dos valores aos nós
no1 = No("Eduardo", 22)
no2 = No("Ana", 35)
no3 = No("Taina", 21)
no4 = No("Wilzão", 20)

#Encadeando nós
no1.proximo = no2
no2.proximo = no3
no3.proximo = no4

imprime(no1)

#Circular
#no4.proximo = no1
