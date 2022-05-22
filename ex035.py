a = int(input('Primeiro segmento:'))
b = int(input('Segundo segmento:'))
c = int(input('Terceiro segmento:'))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triangulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triangulo!')
