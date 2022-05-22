print('=' * 20)
print('{: ^20}'.format('Banco JA'))
print('=' * 20)
valor = int(input('Qual valor você quer sacar? R$'))
if valor >= 50:
    cont50 = valor // 50
    valor = valor % 50
    print(f'Total de {cont50} cédulas de R$50')
if valor >= 20:
    cont20 = valor // 20
    valor = valor % 20
    print(f'Total de {cont20} cédulas de R$20')
if valor >= 10:
    cont10 = valor // 10
    valor = valor % 10
    print(f'Total de {cont10} cédulas de R$10')
if valor >= 1:
    cont1 = valor // 1
    valor = valor % 1
    print(f'Total de {cont1} cédulas de R$1')
print('=' * 20)
print('Volte sempre ao o Banco JA. Tenha um bom dia')
