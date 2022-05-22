peso = float(input('Qual é o seu peso? (kg)'))
altura = float(input('Qual é sua altura? (m)'))
imc = peso/(altura**2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc <= 18.5:
    print('Você esta ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('Você esta no PESO IDEAL')
elif 25 <= imc < 30:
    print('Você esta com SOBREPESO')
elif 30 <= imc <= 40:
    print('Você esta com OBESIDADE')
else:
    print('Você esta com OBESIDADE MÓRBIDA')
