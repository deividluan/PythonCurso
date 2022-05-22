matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for p in range(0, 3):
        matriz[c][p] = int(input(f'Digite um valor para [{c}, {p}]: '))
print('-=' * 30)
for c in range(0, 3):
    for p in range(0, 3):
        print(f'[{matriz[c][p]:^5}]', end='')
    print()
