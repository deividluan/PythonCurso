def metade(n=0, mod=False):
    res = n / 2
    return res if mod is False else moeda(res)


def dobro(n=0, mod=False ):
    res = n * 2
    return res if mod is False else moeda(res)


def aumentar(n=0, t=0, mod=False):
    res = ((n / 100) * t) + n
    return res if mod is False else moeda(res)


def diminuir(n=0, t=0, mod=False):
    res = n - ((n / 100) * t)
    return res if mod is False else moeda(res)


def moeda(n=0, moeda='R$', mod=False):
    return f'{moeda}{n:.2f}'.replace('.', ',')
