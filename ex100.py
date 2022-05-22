from random import randint
from time import sleep
numeros = []
soma = []


def sorteio():
    for c in range(0, 5):
        numeros.append(randint(1, 10))
    print(f'Sorteando 5 valores da lista:', end=' ')
    for c in numeros:
        sleep(0.3)
        print(c, end=' ')
    print()


def somapar():
    for c in numeros:
        if c % 2 == 0:
            soma.append(c)
    print(f'Somando os valores pares de {numeros}, temos {sum(soma)}')


sorteio()
somapar()
