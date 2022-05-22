from random import sample
from time import sleep
lista = []
for c in range(0, 61):
    lista.append(c)
print('=' * 36)
print('{:^36}'.format('JOGO DA MEGA SENA'))
print('=' * 36)
n = int(input('Quantos jogos você quer que eu sorteie? '))
sleep(1)
print('{:-^36}'.format(f' SORTEANDO {n} JOGOS '))
sleep(1)
for c in range(1, n+1):
    sorteio = sample(lista, k=6)
    print(f'Jogo {c}: {sorteio}')
    sleep(1)
print('{:-^36}'.format('< BOA SORTE! >'))
