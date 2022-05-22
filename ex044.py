print('{:=^40}'.format (' LOJA HALAUJ '))
custo = float(input('Preço das compras: R$'))
pagamento = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual opção deseja?'''))
if pagamento == 1:
    total = custo - ((custo/100)*10)
elif pagamento == 2:
    total = custo - ((custo/100)*5)
elif pagamento == 3:
    total = custo
    print(f'Sua compra será parcelada em 2x de R${custo/2} SEM JUROS')
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas?'))
    total = custo + ((custo/100)*20)
    parcelado = total/parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R${parcelado} COM JUROS')
else:
    total = custo
    print('Opção invalida')
print(f'Sua compra de R${custo} vai custar R${total} no final.')