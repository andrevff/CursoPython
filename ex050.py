s = 0
print('Digite 6 números inteiros:')
for c in range(0, 6):
    n = int(input('- '))
    if n % 2 == 0:
        s = s + n
print('Soma dos números pares: {}'.format(s))
