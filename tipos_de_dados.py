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
| - | - | - |
| Base 10 | 11 | 11 |
| Binário | b011 | 3|
| Octal | 0o11 | 9 |
| Hexadecimal | 0x11 | 17 |

#### Conversão de números

| Função | descrição| Resultado |
| - | - | - |
| bin(11) | Converte 11 para binário | 0b1011 |
| hex(11) | Converte 11 para hexa | 0xb|
| oct(11) | Converte 11 para ocatal | 0o13 |
| int(11.1) | Converte 11.1 para inteiro | 11 |
| float(11) | Converte 11 para ponte flutuante | 11.0 |
| complex(11) | Converte 11 para um número complexo | 11+0j |

### Operações com tipos simples

#### Operações aritiméticas com números

| Operador | Descrição | Exemplo | Resultado |
| - | - | - | - |
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
| - | - | - | - |
| + | Soma de dois textos | "Python" + "Python" | PythonPython |  
| * | Multiplicação entre um número e um texto | 2 * "Python" | PyhtonPython |

#### Operações com binários

Vamos usar a função bin, para obter os resultados sempre em binário.

por exemplo: `bin(0b001 ^ 0b100) #'0b101'`
      
      
| Operador | Função | Exemplo | Resultado |
| - | - | - | - |
| >> | | | |
| << | | | |
| and | | | |
| or | | | |
| ^ | | | | |

### Bibliografia
- Borges, E. Luiz - Python para desenvolvedores
- Ramalho, Luciano - Python Fluente
- Summerfild, Mark - Programação em python 3
