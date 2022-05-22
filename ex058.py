from random import randint
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
será que você consegue adivinhar qual foi?''')
computador = randint(0, 10)
n = int(input('Qual é o seu palpite?'))
cont = 1
while n != computador:
    if n < computador:
        print('Mais... Tente mais uma vez.')
    elif n > computador:
        print('Menos... Tente mais uma vez.')
    n = int(input(f'Qual é o seu palpite?'))
    cont += 1
print(f'você acertou com {cont} tentativas. Parabens!!!')
