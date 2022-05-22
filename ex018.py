from math import cos , sin , tan , radians
angulo= float(input('fale um angulo:'))
cosseno = cos(radians(angulo))
seno = sin(radians(angulo))
tangente = tan(radians(angulo))
print(f'O cosseno de {angulo} é \033[34m{cosseno:.2f}\033[m')
print(f'O seno de {angulo} é \033[34m{seno:.2f}\033[m')
print(f'A tangente de {angulo} é \033[34m{tangente:.2f}\033[m')