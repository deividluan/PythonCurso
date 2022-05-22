km = int(input('quantos quilometros você andou com o carro?'))
d = int(input('quantos dias você andou com o carro?'))
pkm= km*0.15
pd= d*60
pf= pkm+pd
print(f'considerando que você andou {km:.2f}km e ficou {d:.2f} dias,fgbn  ficará {pf:.2f}R$ à pagar')