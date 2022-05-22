from random import randint
print('=-' * 15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 15)
resultado = 'Ímpar'
cont = 0
while True:
    n = int(input('Diga um valor: '))
    poui = ' '
    while poui not in 'PI':
        poui = str(input('Par ou impar? [P/I] ')).upper().strip()[0]
    comp = randint(0, 10)
    soma = n + comp
    if soma % 2 == 0:
        resultado = 'Par'
    print('-' * 55)
    print(f'Você jogou {n} e o computador {comp}. Total de {soma} deu {resultado}')
    print('-' * 55)
    if poui in resultado:
        print('Você VENCEU!')
    else:
        print('Você PERDEU!')
        break
    cont += 1
    print('=-' * 15)
print(F'GAME OVER! Você venceu {cont} vezes.')
