nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
media = (nota1+nota2)/2
print(f'Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}')
if 7 > media > 5:
    print(f'O aluno esta de RECUPERAÇÃO')
elif media >= 7:
    print(f'O aluno foi APROVADO')
elif media < 5:
    print(f'O aluno foi REPROVADO')
