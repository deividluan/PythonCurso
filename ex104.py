def leiaint(msg):
    print('-' * 25)
    while True:
        n = str(input(msg))
        if n.isnumeric():
            return n
            break
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')


#Programa principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
