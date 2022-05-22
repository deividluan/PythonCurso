import moeda

num = float(input('Digite um preço: R$'))
taxa = 10
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'Aumentando {taxa}%, temos {moeda.moeda(moeda.aumentar(num, taxa))}')
