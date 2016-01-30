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

### Bibliografia
- Borges, E. Luiz - Python para desenvolvedores
- Ramalho, Luciano - Python Fluente
- Summerfild, Mark - Programação em python 3
