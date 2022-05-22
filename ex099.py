from time import sleep


def maior(*num):
    print('-=' * 30)
    print('Analizando os valores passados...')
    if len(num) > 0:
        for c in num:
            print(c, end=' ')
            sleep(0.3)
    print(f'foram informadas {len(num)} valores ao todo.')
    print(f'O maior valor informado foi ', end='')
    if len(num) == 0:
        print(0)
    else:
        print(max(num))


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
