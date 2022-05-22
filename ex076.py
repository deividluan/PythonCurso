print('-' * 40)
print('{: ^40}'.format('Bar do Batista'))
print('-' * 40)
cont = 0
menu = ('Lápis', 1.75,
        'borracha', 2.00,
        'caderno', 15.00,
        'estojo', 4.00,
        'transferidor', 4.00,
        'compasso', 9.99,
        'mochila', 120.32,
        'canetas', 22.30,
        'livros', 34.90,)
for cardapio in range(0, len(menu)):
        if cardapio % 2 == 0:
                print(f'{menu[cardapio]:.<30}', end='')
        else:
                print(f'R${menu[cardapio]:>7.2f}')
print('-' * 40)
