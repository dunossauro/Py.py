"""
Exemplos de uso do signature
"""

from inspect import signature

"""
Testes com lambda
"""

test_1 = lambda x, y=7: (x, y)

print(test_1.__name__)
print(test_1.__annotations__)

sig_1 = signature(test_1)

print(sig_1.parameters.items())

for name, param in sig_1.parameters.items():
    print(param.kind)

"""
Funções normais
"""

def test_2(x: int, y:[str, int]) -> None:
    pass

print(test_2.__name__)
print(test_2.__annotations__)

sig_2 = signature(test_2)

print(sig_2.parameters.items())

for name, param in sig_2.parameters.items():
    print(param.kind)
