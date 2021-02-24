n1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
decimo = n1 + (10 - 1) * r
for c in range(n1, decimo + r, r):
    print('{} '.format(c))
