soma = 0
mais1000 = 0
c = 0
menor = 0
barato = ' '
print('='*30)
print('LISTA DE COMPRAS'.center(27))
print('='*30)
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: '))
    print('-'*30)
    soma += preco
    if preco > 1000:
        mais1000 += 1
    if c == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome
    op = str(input('Deseja continuar? [S/N]: '))
    print('-'*30)
    if op in 'Nn':
        break
print(f'Valor total da compra: R${soma:.2f}')
print(f'{mais1000} produtos custam mais de R$1000,00')
print(f'O produto mais barato foi o(a) {barato}')
