import random

def gen():
    """Função que gera o baralho."""
    nipes = ["paus", "ouro", "espada", "copas"]

    cartas = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

    baralho = []
    for x in cartas:
        for y in nipes:
            gen_baralho = x, y
            baralho.append(gen_baralho)
    baralho.append("coringa")

    return baralho


def shuffle(baralho):
    random.shuffle(baralho)
    return baralho


baralho = gen()
embaralhado = shuffle(baralho)

for cartas in embaralhado:
    print(cartas)
