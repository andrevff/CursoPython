c = 1
c2 = 1
n1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
while c <= 10:
    print('{} '.format(n1))
    n1 += r
    c += 1
while c2 != 0:
    c2 = int(input('Deseja mostrar mais quantos números?'))
    c = 1
    while c <= c2:
        print('{} '.format(n1))
        n1 += r
        c += 1
