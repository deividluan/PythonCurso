def metade(n=0):
    res = n / 2
    return res


def dobro(n=0):
    res = n * 2
    return res


def aumentar(n=0, t=0):
    res = ((n / 100) * t) + n
    return res


def diminuir(n=0, t=0):
    res = n - ((n / 100) * t)
    return res


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')