palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PHYTHON', 'CURSO',
            'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
            'PROGRAMADOR', 'FUTURO')
for c in palavras:
    print(f'\nNa palavra {c} temos', end=' ')
    for conferir in c:
        if conferir in 'AEIOU':
            print(conferir, end=' ')
