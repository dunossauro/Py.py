## Tipos de dados em Python

Nesse pequeno artigo, será introduzido o conseito de tipos de dados em Python.

Em Python, existem dois tipos de dados:

      1. Simples: Numeros inteiros, complexos, de ponto flutuante e texto (strings)

      2. Colecionáveis: Como strings, tuplas, listas, conjuntos e dicionários

Pode-se atribuir qualquer tipo de dados a um variável, como por exemplo:

> num = 5

o valor 5 foi atribuído a variável num

#### Função type

Caso exista a necessidade de saber qual tipo de dado esta sendo manipulado, pode-se usar a função `type(tipo_de_dado)`

por exemplo:

                  >>> type(5)
                  int
                  >>> type(5.0)
                  float
                  >>> type(5 + 1j)
                  complex
            

### Numeros inteiros

| Tipo | Chamada | Resultado |
|--------------|--------------|--------------|
| Base 10 | 11 | 11 |
| Binário | b011 | 3|
| Octal | 0o11 | 9 |
| Hexadecimal | 0x11 | 17 |

#### Conversão de números

| Função | descrição| Resultado |
|--------------|--------------|--------------|
| bin(11) | Converte 11 para binário | 0b1011 |
| hex(11) | Converte 11 para hexa | 0xb|
| oct(11) | Converte 11 para ocatal | 0o13 |
| int(11.1) | Converte 11.1 para inteiro | 11 |
| float(11) | Converte 11 para ponte flutuante | 11.0 |
| complex(11) | Converte 11 para um número complexo | 11+0j |

### Operações com tipos simples

#### Operações aritiméticas com números

| Operador | Descrição | Exemplo | Resultado |
|--------------|--------------|--------------|--------------|
| + | soma de dois valores| 5 + 3 | 8 |
| + | Atribui valor posítivo a um número |+5 | 5 |
| - | subtração de dois valores | 5 - 3 | 2 |
| - | Atribui valor negativo a um número | -5 | -5 |
| * | multiplicação de dois valores | 5 * 3 | 15 |
| / | Divisão entre dois valores | 5 / 3 | 1.6666666666666667 |
| // | Divisão inteira entre dois valores | 5 // 3 | 1 |
| % | Modulo, ou resto de da divisão entre dois valores| 5 % 3 | 2 |
| ** | Potência entre dois números | 2**3 | 8 |

#### Operações aritiméticas com texto

| Operador | Função | Exemplo | Resultado |
|--------------|--------------|--------------|--------------|
| + | Soma de dois textos | "Python" + "python" | Pythonpython |  
| * | Multiplicação entre um número e um texto | 2 * "Python" | PythonPython |

#### Operações com binários

Vamos usar a função bin, para obter os resultados sempre em binário.

por exemplo: `bin(0b001 ^ 0b100) #'0b101'`


| Operador | Função | Exemplo | Resultado |
|--------------|--------------|--------------|--------------|
| >> | Deslocar bits a direita| bin(0b100 >> 2) | 0b1 |
| << | Deslocar bits a esquerda| bin(0b100 << 2)| 0b10000 |
| and | Operador lógico 'E'| bin(0b100 and 0b010) | 0b10 |
| or | Operador lógico 'OU'| bin(0b100 or 0b010) | 0b100 |
| ^ | Operador lógico 'XOR'| bin(0b100 ^ 0b010)| 0b110|

#### Operadores de comparação

| Operador | Função | Exemplo | Resultado |
|--------------|--------------|--------------|--------------|
| > | Operador 'maior que' | 4 > 3 | True|
| >= | Operador 'maior igual' | 4 >= 3 | True |
| < | Operador 'menor que' | 4 < 3 | False |
| <= | Operador 'menor igual' | 4 <= 3| False |
| == | Operador de igualdade | 4 == 3| False|
| != | Operador de diferença | 4 != 3| True |


# Listas em python3

## Declaração de listas

Para declarar uma lista, podemos usar a função 'list()' de qualquer iterável.

por exemplo:

      >> lista = list("eduardo")
      >>print(lista)
      ['e','d','u','a','r','d','o']


## Métodos de uma lista (Tabela para preguiçosos)

| Método | Função |
|----------|----------|
| append | Insere um elemento no final da lista |
| copy | Faz um cópia da lista |
| count | Conta quantas vezes um elemento está presente na lista |
| extend | Faz a união entre duas listas |
| index | Retorna a primeira posição de um elemento |
| insert | insere um elemento na lista |
| pop | Remove o ultimo elemento da lista e printa na tela |
| remove | Remove um elemento da lista |
| reverse | Inverte a lista, sem a atribuição a outra variável |
| sort | Organiza a lista em ordem alfabética |


### Exemplos

> Para todos os exemplos usaremos uma lista decalara da segunte maneira: lista = [1,2,3,4]

#### append
O método append pode ser usado para inserir um elemento, independente de seu tipo, no final de uma lista

            >> lista.append('x')
            >> print(lista)
            [1,2,3,4, 'x']

#### copy
O método copy faz um copia integral de uma lista, por exemplo:

            >> lista2 = lista.copy()
            >> print(lista2)
            [1,2,3,4,5]

Vale lembrar que usando o slice também conseguiriamos uma cópia parecida

            >> lista2 = lista[:]
            >> print(lista2)
            [1,2,3,4,5]

#### count
O método count conta quantos elementos iguais existem dentro de uma lista

            >> lista.count(3)
            1

#### extend
O método extend concatena os elementos de um lista a lista que envocou o método, por exemplo:

            >> lista = [0,0,0]
            >> lista_2 = [1,1,1]
            >> lista.extend(lista_b)
            >> print(lista)
            [0,0,0,1,1,1]

#### index
O método index retorna a primeira aparição de um elemento na lista, por exemplo:

            >> lista = [1,0,0]
            >> lista.index(0)
            1

#### insert
O método index insere um elemento, em alguma posição, na lista, por exemplo:

           >> lista.insert(1,'a')
           >> print(lista)
           [1,'a',2,3,4]

#### pop
O método pop, trabalha como a estrutura de pilha (ou FIFO), ou seja, ele remove a ultima posição da lista e printa na tela.

            >> lista.pop()
            4

#### remove
O método remove, remove da lista o primeiro elemento passado como argumento. Ou seja, trabalha de maneira similar ao index, só que na deleção de elementos

            >> lista = list("baba")
            >> lista.remove('b')
            >> print(lista)
            ['a', 'b', 'a']

#### reverse e sort
O método reverse, inverte a lista. Mas sem a necessidade de atribuição a outra lista

            >> lista.reverse()
            >> print(lista)
            [4,3,2,1]

Já o método sort, ordena a lista em ordem alfabética, vamos usar a lista gerada com o reverse como exemplo.

            >> lista.sort()
            >> print(lista)
            [1,2,3,4]

> Obs: o sort usa a tabela ASCII como referência, o que pode fazer os caracteres acentuados não entrarem na ordem correta.

## Compreensão de listas


## matrizes com listas

### Bibliografia
- Borges, E. Luiz - Python para desenvolvedores
- Ramalho, Luciano - Python Fluente
- Summerfild, Mark - Programação em python 3
