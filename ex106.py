def lin(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    from time import sleep
    sleep(1)


while True:
    print('\033[42;97m')
    lin('Sistema de ajuda PyHelp')
    print('\033[m')
    r = input('Função ou Biblioteca > ').lower()
    if r in 'fim':
        print('\033[97;41m')
        lin('ATÉ LOGO!')
        print('\033[m')
        break
    else:
        print('\033[44;97m')
        lin(f'Acessando o manual do comando {r}')
        print('\033[m')
        print('\033[30;107m')
        help(r)
        print('\033[m')
