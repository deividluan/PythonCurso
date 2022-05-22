from datetime import date
ano = int(input('Ano de nascimento:'))
atual = date.today().year
idade = atual - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {atual}')
# menor de 18
if idade < 18:
    falta = 18 - idade
    adiantado = falta + atual
    print(f'''Ainda falta {falta} anos para o alistamento.
Seu alistamento será em {adiantado}''')
# maior de 18
elif idade > 18:
    devendo = idade - 18
    atrasado = atual - devendo
    print(f'''Você já deveria ter se alistado há {devendo} anos.
Seu alistamento foi em {atrasado}''')
# tem 18
else:
    print(f'Você tem que se alistar IMEDIATAMENTE!')
