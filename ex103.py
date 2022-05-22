def ficha(jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato')


print('-' * 25)
j = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if j.strip() == '':
    ficha(gols=g)
else:
    ficha(j, g)
