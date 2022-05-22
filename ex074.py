from random import randint
tupla = (randint(0, 10), randint(0, 10),
         randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os Valores sorteados foram: {tupla}')
print(f'O maior valor sorteado foi {max(tupla)}')
print(f'O menor  valor sorteado foi {min(tupla)}')
