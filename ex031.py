km = float(input('Digite a distancia da sua viajem:'))
print(f'Você esta prestes a começar uma viagem de {km}km')
if km <= 200:
    passagem1 = km * 0.50
    print(f'E o preço da sua passagem será de R${passagem1:.2f}')
else:
    passagem2 = km * 0.45
    print(f'E o preço da sua passagem será de R${passagem2:.2f}')
