import moeda

num = float(input('Digite um preço: R$'))
taxa = 50
print(f'A metade de R${num:.2f} é R${moeda.metade(num):.2f}')
print(f'O dobro de R${num:.2f} é R${moeda.dobro(num):.2f}')
print(f'Aumentando {taxa}%, temos R${moeda.aumentar(num, taxa):.2f}')
