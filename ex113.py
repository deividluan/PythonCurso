def leiaint(n):
    while True:
        try:
            i = int(input(n))
        except:
            print('\033[31mERRO! Digite um número inteiro valido\033[m')
        else:
            break
    return i


def leiafloat(n):
    while True:
        try:
            r = float(input(n))
        except:
            print('\033[31mERRO! Digite um número real valido\033[m')
        else:
            break
    return r


i = leiaint('Digite um número inteiro: ')
r = leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {i} o real {r}')
