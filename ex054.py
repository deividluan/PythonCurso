from datetime import date
cont = 0
cont1 = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}ª pessoa nasceu?'))
    atual = date.today().year
    idade = atual - ano
    if idade < 18:
        cont += 1
    else:
        cont1 += 1
print(f'Ao todo temos {cont1} pessoas maiores de idade')
print(f'Ao todo temos {cont} pessoas menores de idade')
