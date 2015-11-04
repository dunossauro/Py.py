## Projeto de Linguistica de Corpus

Nome Proposto: TNWST (This is not Word Smith Tools)

Esse projeto tem como objetivo suprir as necessidades do WordSmithTools

V: 0.0.2

L: GPL 3

###### Dependências: NLTK, TKinter.



#Comentários a comunidade da Python Brasil

Existe um programa que lida com linguistica de corpus, na verdade oferece algumas ferramentas importantes para os linguistas de corpus. Se chama WordSmithTools[1]. 

Ele oferece

3 Ferramentas:

  ####1. Wordlist:
    1.1 Lista palavras individuais (como um contador de palavras)
    1.2 List de multipalavras (É um contador de ocorrências de palavras específicas)
    1.3 Oferece suporte a ordenar por ordem alfabética ou por ordem de frequência
    1.4 Dá porcentagem de ocorrência no texto
    1.5 Lista também palavras com o mesmo radical (Des/prefixo Graça/Radical)

  ####2. Concord
    2.1 Concordância (Por exemplo, se buscarmos a palavra 'como': Ele/E2 come/E1 como/C um/D1 leão/D2), [busca as palavras da mesma frase]
    2.2 Lista de alocados (Lista os colocados da direita e esquerda, como no exemplo anterior)
    2.3 Lista de agrupamentos lexicais (Podemos escolher todas as frases em que 'Ele' está na posição E2 e 'como' no centro)
    2.4 Gráfico de distribuição de frequência (Um plot de de todas as vezes em que a palavra aparece em um texto)
    2.5 Existe a opção de ordenar cada (Esquerda ou direita) em relação ao centro.

  ####3. Keyword
    3.1 Compara duas contagens de palavras, após serem usadas no WordList (Contagem e porcentagem)
    3.2 Também pode ser organizado alfabéticamente e por ocorrência
    3.3 Lista elos entre palavras chave

[1]:http://www.lexically.net/wordsmith/
