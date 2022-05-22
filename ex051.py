print('='*30)
print('    10 termos de uma PA  ')
print('='*30)
n = int(input('Primeiro termo:'))
r = int(input('Razão:'))
f = (n + (10 - 1) * r) + r
for c in range(n, f, r):
    print(c, end=' → ')
print('Fim')