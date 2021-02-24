n = 0
cont = 0
media = 0
maior = 0
menor = 0
op = ' '
while op not in 'Nn':
    n = int(input('Digite um número: '))
    media += n
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    op = str(input('Quer continuar? [S/N]: '))
print('Média entre os números {:.2f}'.format(media/cont))
print('Maior número: {}'.format(maior))
print('Menor número: {}'.format(menor))
