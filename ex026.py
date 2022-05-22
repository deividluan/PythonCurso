n = str(input('digite uma frase:')).strip().upper()
print(f'A letra A aparece {n.count("A")} vezes na frase')
print(f'A primeira letra A aparece na posição {n.find("A")+1}')
print(f'A ultima letra A apareceu na posição {n.rfind("A")+1}')
