from datetime import date
work = {}
work['nome'] = str(input('Nome: '))
work['idade'] = int(input('Ano de nascimento: '))
work['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
work['idade'] = date.today().year - work['idade']
if work['CTPS'] != 0:
    work['contratação'] = int(input('Ano de contratação: '))
    work['salário'] = float(input('Salário: R$'))
    work['aposentadoria'] = work['idade'] + ((work['contratação'] + 35) - date.today().year)
print('-=' * 20)
for k, v in work.items():
    print(f'  - {k} tem valor {v}')
