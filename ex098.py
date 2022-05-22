from time import sleep


def cont(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        for c in range(i, f+1, p):
            print(c, end=' ')
            sleep(0.3)
    else:
        cont = i
        while cont >= f:
                print(cont, end=' ')
                cont -= p
                sleep(0.3)
    print(' FIM!')


def lin():
    print('-=' * 20)


lin()
cont(1, 10, 1)
lin()
cont(10, -2, 2)
lin()
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
lin()
cont(inicio, fim, passo)
