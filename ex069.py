homens = maior = menor = 0
while True:
    print('-' * 25)
    print('CADASTRE UMA PESSOA')
    print('-' * 25)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] ')).strip()[0]
    print('-' * 25)
    if sexo in 'Mm':
        homens += 1
    if idade >= 18:
        maior += 1
    if idade < 20 and sexo in 'Ff':
        menor += 1
    duvida = ' '
    while duvida not in 'SsNn':
        duvida = str(input('Quer continuar? [S/N] ')).strip()[0]
    if duvida in 'Nn':
        break
print(f'Total de pessoas com mais de 18 anos: {maior} ')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {menor} mulheres com menos de 20 anos')