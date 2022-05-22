n1 = int(input('digite a nota da sua prova: '))
n2 = int(input('digite a nota do seu trabalho:'))
m = (n1+n2)/2
if m >= 6:
    print(f'sua média é \033[34m{m}\033[m, \033[32mvocê foi muito bem!!!')
else:
    print(f'Sua média é \033[31m{m}\033[m,\033[31m você foi muito mal!!!')
