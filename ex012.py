preco = float(input('Digite o preço do produto: '))
desc = preco * (5/100)
final = preco - desc
print('Valor do produto com o desconto: R$ {:.2f}'.format(final))
