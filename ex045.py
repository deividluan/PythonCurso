from random import randint
from time import sleep
lista = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input(f'Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*11)
print(f'O Computador jogou {lista[computador]}')
print(f'O Jogador jogou {lista[jogador]}')
print('-='*11)
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('\033[34m EMPATE\033[m')
    elif jogador == 1:
        print('\033[32m O JOGADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[31m O COMPUTADOR VENCE\033[m')
    else:
        print('JOGADA INVALIDA')
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('\033[31m O COMPUTADOR VENCE\033[m')
    elif jogador == 1:
        print('\033[34m EMPATE\033[m')
    elif jogador ==2:
        print('\033[32m O JOGADOR VENCE\033[m')
    else:
        print('JOGADA INVALIDA')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('\033[32m O JOGADOR VENCE\033[m')
    elif jogador == 1:
        print('O \033[31m O COMPUTADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[34m EMPATE\033[m')
    else:
        print('JOGADA INVALIDA')
