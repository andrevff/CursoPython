color = {
    'clean': '\033[m',
    'b_green': '\033[42m',
    'l_green': '\033[32m',
    'under': '\033[7m'
}
print('{} CAIXA {}'.format(color['b_green'], color['clean']).center(37))
print('-'*30)
preco = float(input('Informe o preço do produto: '))
print('-'*30)
print('{} Formas de pagamento {}'.format(color['under'], color['clean']).center(37))
print('1 - A vista (dinheiro/cheque)')
print('2 - A vista (cartão)')
print('3 - Em até 2X no cartão')
print('4 - 3X ou mais (juros)')
print('-'*30)
i = int(input('Digite a opção e pressione ENTER: '))
print('-'*30)
if i == 1:
    pag = preco - (preco * (10 / 100))
    print('Valor a pagar: {}R$ {:.2f}{}'.format(color['l_green'], pag, color['clean']))
elif i == 2:
    pag = preco - (preco * (5 / 100))
    print('Valor a pagar: {}R$ {:.2f}{}'.format(color['l_green'], pag, color['clean']))
elif i == 3:
    pag = preco
    print('Valor a pagar: {}R$ {:.2f}{}'.format(color['l_green'], pag, color['clean']))
else:
    pag = preco + (preco * (20 / 100))
    print('Valor a pagar: {}R$ {:.2f}{}'.format(color['l_green'], pag, color['clean']))
