#Importação dos aquivos gerais.
from os import system
from contador_de_palavras import contagem
from concordancia import concord
from comparacao import compare
"""
from tagger import tag
"""
def main():
    system("clear")
    print("\
                 ####TNSWT####\n\
            \n\
            \n\
            1. Contador de palavras:\n\
            2. Concordancia:\n\
            3. Comparação:\n\
            4. Tagger:\n\n\
            5. Sair\n\n")

    choice = int(input('Digite a opção desejada: '))

    if choice is 1:
        contagem()
   
    elif choice == 2:
        concord()
    
    elif choice == 3:
        compare()
    
    elif choice == 5:
        tag()
    
    elif choice == 4:
        exit

if __name__ == '__main__':
    main()
