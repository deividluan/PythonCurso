cont = soma = n = 0
n = int(input('Digite um numero [999 para parar]:'))
while not n == 999:
    soma += n
    cont += 1
    n = int(input('Digite um numero [999 para parar]:'))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')
