n = 0
soma = 0
cont = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        cont += 1
        soma += n
print('Você digitou {} números'.format(cont))
print('A soma entre eles é {}'.format(soma))
