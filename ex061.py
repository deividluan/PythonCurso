print('Gerador de PA')
print('-=' * 20)
pt = int(input('Primeiro termo:'))
r = int(input('Razão da PA:'))
cont = 1
termo = pt
while cont <= 10:
    print(termo, end=' → ')
    termo += r
    cont += 1
print('FIM')
