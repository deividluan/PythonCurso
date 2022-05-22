def mult(a, b):
    s = a * b
    print(f'A área do terreno {a} x {b} é {s:.2f}²')


print('Controle de Terrenos')
print('-' * 20)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
mult(largura, comprimento)
