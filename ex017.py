from math import pow, sqrt
co = int(input('digite o comprimento do cateto oposto:'))
ca = float(input('digite o comprimento do cateto adjacente:'))
coxx2 = pow(co , 2)
caxx2 = pow(ca, 2 )
soma = coxx2 + caxx2
raiz = sqrt(soma)
print(f'a potencia do cateto oposto é {coxx2}')
print(f'a potencia do cateto adjacente é {caxx2}')
print(f'a raiz dá soma entre os dois é {raiz}')