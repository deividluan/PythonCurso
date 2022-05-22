matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = coluna3 = mai = 0
for c in range(0, 3):
    for p in range(0, 3):
        matriz[c][p] = int(input(f'Digite um valor para [{c}, {p}]: '))
        if matriz[c][p] % 2 == 0:
            soma += matriz[c][p]
print('-=' * 20)
for c in range(0, 3):
    for p in range(0, 3):
        print(f'[{matriz[c][p]:^5}]', end=' ')
        if p == 2:
            coluna3 += matriz[c][p]
        if p == 1:
            mai = max(matriz[1])
    print()
print(f'-=' * 20)
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {coluna3}')
print(f'O maior valor da segunda linha é o {mai}')
