print('-' * 20)
print('  Loja Baratovisc')
print('-' * 20)
tot = maior = custo = cont = 0
barato = ''
while True:
    n = str(input('Nome do produto:'))
    p = float(input('Preço: R$'))
    cont += 1
    tot += p
    if p > 1000:
        maior += 1
    if cont == 1 or p < custo:
        custo = p
        barato = p
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    print('-' * 30)
    if perg == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi {tot}')
print(f'Temos {maior} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${custo}')
