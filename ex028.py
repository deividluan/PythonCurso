import random
from time import sleep
print('Vou pensar em um numero de 0 a 5. Tente adivinhar...')
numero = int(input('Em que numero eu pensei?'))
lista = [0, 1, 2, 3, 4, 5]
valor = random.choice(lista)
print('PROCESSANDO...')
sleep(3)
if numero == valor:
    print(f'PARABENS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no numero {valor} e não no {numero}')
