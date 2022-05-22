n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o ultimo número: '))
tupla = (n1, n2, n3, n4)
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apreceu na posição {tupla.index(3)+1}ª posição')
else:
    print(f'Você não digitou o número 3')
print(f'Os valores pares digitados foram ', end='')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')
