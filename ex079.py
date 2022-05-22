lista = []
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    if n in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(n)
        print('Valor adicionado com sucesso..')
    r = str(input('Quer continuar: [S/N] ')).upper()
print('-=' * 20)
print(f'Você digitou os valores {lista}')
