from time import sleep
n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
escolha = 0
while escolha != 5:
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos numeros
[ 5 ] Sair do programa''')
    escolha = int(input('>>>> Qual é a sua opção? '))
    if escolha == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}')
    elif escolha == 2:
        multiplicar = n1 * n2
        print(f'O resultado de {n1} x {n2} é {multiplicar}')
    elif escolha == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior valor é {n1}')
        elif n2 > n1:
            print(f'Entre {n1} e {n2} o maior valor é {n2}')
        elif n2 == n1:
            print(f'Ambos são iguais')
    elif escolha == 4:
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))
    elif escolha == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('-=' * 20)
    sleep(1)
sleep(1)
print('Fim do programa! Volte sempre!')
