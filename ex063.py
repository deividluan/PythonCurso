fibo = 1
cont = 0
numero = 0
soma = 0
print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
while not cont == n:
    anterior = soma
    print(soma, end=' → ')
    soma += fibo
    fibo = anterior
    cont += 1
print('Fim')
