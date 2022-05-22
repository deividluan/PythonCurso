print('-' * 20)
def voto(n=0):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÂO VOTA'
    elif idade >= 18 or idade < 65:
        return f'Com {idade} anos: VOTA'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'

ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
