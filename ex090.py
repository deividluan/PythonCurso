aluno = {}
aluno['nome'] = (str(input('Nome: ')))
aluno['média'] = (float(input(f'Média de {aluno["nome"]}: ')))
if aluno['média'] >= 7:
    aluno['situação'] = 'APROVADO'
elif aluno['média'] < 5:
    aluno['situação'] = 'REPROVADO'
else:
    aluno['situação'] = 'Recuperação'
print('-=' * 20)
print(aluno)
for k, v in aluno.items():
    print(f'    - {k} é igual a {v}')
