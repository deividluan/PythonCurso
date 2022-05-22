maior = 0
menor = 0
soma = 0
coroa = ''
for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).upper()
    soma += idade
    if sexo == 'M':
        if c == 1:
            maior = idade
            coroa = nome
        else:
            if idade > maior:
                maior = idade
                coroa = nome
    if sexo == 'F':
        if idade < 20:
            menor += 1
media = soma / 4
print(f'A média de idade do grupo é de {media} anos')
print(f'O Homem mais velho tem {maior} anos e se chama {coroa}')
print(f'Ao todo são {menor} mulheres com menos de 20 anos')
