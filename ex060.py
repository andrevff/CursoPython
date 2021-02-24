fat = 1
c = 1
n = int(input('Digite um número: '))
while c <= n:
    fat *=c
    c += 1
print('Fatorial de {}: {}'.format(n, fat))
