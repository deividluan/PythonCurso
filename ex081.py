lista = []
r = 'S'
while 'S' in r:
    n = lista.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('-=' * 20)
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrecente são {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista!')
else:
    print(f'O vaor 5 não faz parte da lista!')
