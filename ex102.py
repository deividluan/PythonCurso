def fatorial(n=1, show=False):
    """
    --> Faz um calculo fatorial com o número informado
    :param n: Número a ser calculado.
    :param show: (opcional) mostra como foi feito o calculo.
    :return: O valor do fatorial do n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c} x', end=' ')
        f *= c
    if show:
        print('=', end=' ')
    return f

print(fatorial(5, True))
#help(fatorial)