lista = []
for c in range(0, 5):
    n = lista.append(int(input(f'Digite um valor para a Posição {c}: ')))
print(f'Você digitou os valores {lista}')
maior = max(lista)
menor = min(lista)
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for pos, p in enumerate(lista):
    if p == maior:
        print(pos, end='... ')
print(f'\nO menor valor digitado foi {menor}, nas posições ', end='')
for pos, p in enumerate(lista):
    if p == menor:
        print(pos, end='... ')
