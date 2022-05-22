from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
for v in range(1, 5):
    jogadores[f'jogador{v}'] = randint(1, 6)
print('Valores Sorteados: ')
for k, v in jogadores.items():
    sleep(1)
    print(f'{k} tirou {v} no dado.')
print('-=' * 20)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('    == RANKING DOS JOGADORES ==')
for k, v in enumerate(ranking):
    sleep(1)
    print(f'     {k+1}° lugar: {v[0]} com {v[1]}')
