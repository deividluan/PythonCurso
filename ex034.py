salario = float(input('digite seu salario:'))
if salario >= 1250:
    salariomaior = ((salario / 100) * 10) + salario
    print(f'Seu salario de R${salario:.2f} passara para R${salariomaior:.2f}')
else:
    salariomenor = ((salario/100) * 15) + salario
    print(f'Seu salario de R${salario:.2f} passara para R${salariomenor:.2f}')

