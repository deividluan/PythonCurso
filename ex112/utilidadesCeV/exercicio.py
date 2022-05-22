import moeda

num = moeda.leiadinheiro('Digite um preço: R$')
taxa = 10
desconto = 13
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'Aumentando {taxa}%, temos {moeda.aumentar(num, taxa, True)}')
print(f'Diminuindo {desconto}% temos {moeda.diminuir(num, taxa, True)}')
