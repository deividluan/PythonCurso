lista = []
pares = []
impares = []
r = 'S'
while 'S' in r:
    n = (int(input('Digite um valor: ')))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 == 1:
        impares.append(n)
    r = str(input('Deseja continuar? [S/N] ')).upper()
print('-=' * 20)
print(f'A lista completa {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
