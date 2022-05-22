dado = []
galera = []
r = 'S'
men = mai = 0
while r in 'S':
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    if len(galera) == 0:
        mai = men = dado[1]
    else:
        if mai < dado[1]:
            mai = dado[1]
        if men > dado[1]:
            men = dado[1]
    galera.append(dado[:])
    dado.clear()
    r = str(input('Quer continuar? [S/N] ')).upper()
print('-=' * 20)
print(f'Ao todo, você cadastrou {len(galera)} pessoas')
print(f'O maior peso foi de {mai}Kg. Peso de', end=' ')
for p in galera:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {men}Kg. Peso de', end=' ')
for p in galera:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')
