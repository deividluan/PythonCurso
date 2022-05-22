a = float(input('Primeiro segmento:'))
b = float(input('Segundo segmento:'))
c = float(input('terceiro segmento:'))
if a < b + c and b < a + c and c < b + a:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if a == b == c:
        print('EQUILATERO')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('Não é possivel formar um triangulo')