tabela = ('atletico-MG', 'Palmeiras', 'Flamengo', 'Bragantino', 'Fortaleza',
          'Corinthians', 'Internacional', 'Fluminense', 'Cuiabá', 'Ceará SC',
          'Athletico-PR', 'América-MG', 'Atlético-GO', 'São Paulo', 'Bahia',
          'Santos', 'Sport Recife', 'Juventude', 'Gremio', 'Chapecoense')
print('-=' * 20)
print(f'Lista de times do Brasileirão: {tabela}')
print('-=' * 20)
print(f'Os 5 primeiros são: {tabela[:5]}')
print('-=' * 20)
print(f'Os 4 ultimos são: {tabela[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-=' * 20)
print(f'O Chapecoense está na {tabela.index("Chapecoense")+1}ª posição')
