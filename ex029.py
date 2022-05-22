velocidade = float(input('Qual é a velocidade atual do carro?'))
if velocidade > 80:
    print(f'MULTADO! Você excedeu o limite permitido que é de 80km/h!')
    multa = (velocidade - 80)*7
    print(f'Você deve pagar uma multa de R${multa}!')
    print(f'Tenha um PESSIMO dia! Dirija com segurança!')
else:
    print(f'Tenha um bom dia! Dirija com segurança')
