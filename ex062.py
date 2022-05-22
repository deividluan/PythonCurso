print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro Termo:'))
razao = int(input('Razão:'))
cont = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, end=' → ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos quer mostrar a mais?'))
print(f'Progreção finalizada com {total} termos mostrados')
