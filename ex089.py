turma = []
r = 'S'
while 'S' in r:
    nome = (str(input('Nome: ')))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    turma.append([nome, [nota1, nota2], média])
    r = str(input('Deseja continuar? [S/N] ')).upper()
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"Média":>8}')
print('-' * 26)
for i, a in enumerate(turma):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(turma) - 1:
        print(f'Notas de {turma[opc][0]} são {turma[opc][1]}')
print('<<< Volte sempre >>>')