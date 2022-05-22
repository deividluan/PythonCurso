def notas(*pontos, sit=False):
    """
    -> Analisa a nota de varios alunos e fala algumas informações sobre
    :param pontos: uma ou mais notas dos alunos
    :param sit: (opcional) Mostra a situação da turma
    :return: Dicionario com varias informações
    """
    soma = 0
    turma = {}
    print('-=' * 20)
    turma['total'] = len(pontos)
    turma['maior'] = max(pontos)
    turma['menor'] = min(pontos)
    turma['média'] = sum(pontos) / len(pontos)
    if sit:
        if turma['média'] < 5:
            turma['situação'] = 'RUIM'
        if turma['média'] >= 7:
            turma['situação'] = 'BOA'
        if 7 > turma['média'] > 5:
            turma['situação'] = 'RAZOÁVEL'
    print(turma)


#Programa principal
resp = notas(10, 10, 6, 6.5, sit=True)
help(notas)