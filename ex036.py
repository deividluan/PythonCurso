casa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
f = int(input('Quantos anos de financiamento?'))
precof = casa/(f*12)
porcentagem = (salario/100)*30
print(f'Para pagar uma casa de R${casa:.2f} em {f} anos  a prestação será de R${precof:.2f}')
if precof > porcentagem:
    print(f'Empréstimo NEGADO!')
else:
    print(f'Empréstimo pode ser CONCEDIDO!')
