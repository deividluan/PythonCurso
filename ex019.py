import random
a1 = str(input('fale o nome do primeiro aluno:'))
a2 = str(input('fale o nome do segundo aluno:'))
a3 = str(input('fale o nome do terceiro aluno:'))
a4 = str(input('fale o nome do quarto aluno:'))
l= [a1, a2, a3, a4]
e= random.choice(l)
print(f'O aluno escolhido foi {e}')
