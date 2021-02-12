color = {
    'clean': '\033[m',
    'b_oran': '\033[43m',
    'l_blue': '\033[34m',
    'l_oran': '\033[33m',
    'l_red': '\033[31m'
}
print('{} CONVERSOR DE NÚMEROS {}'.format(color['b_oran'], color['clean']).center(30))
print('-'*22)
print('{}1{} - {}Binário{}'.format(color['l_blue'], color['clean'], color['l_oran'], color['clean']))
print('{}2{} - {}Octal{}'.format(color['l_blue'], color['clean'], color['l_oran'], color['clean']))
print('{}3{} - {}Hexadecimal{}'.format(color['l_blue'], color['clean'], color['l_oran'], color['clean']))
print('-'*20)
i = int(input('Digite a opção e pressione ENTER: '))
if i == 1:
    n = int(input('Digite o número que deseja converter: '))
    print('O número {}{}{} convertido em binário é {}{}{}'.format(color['l_oran'], n, color['clean'], color['l_oran'], bin(n)[2:], color['clean']))
elif i == 2:
    n = int(input('Digite o número que deseja converter: '))
    print('O número {}{}{} convertido em octal é {}{}{}'.format(color['l_oran'], n, color['clean'], color['l_oran'], oct(n)[2:], color['clean']))
elif i == 3:
    n = int(input('Digite o número que deseja converter: '))
    print('O número {}{}{} convertido em hexadecimal é {}{}{}'.format(color['l_oran'], n, color['clean'], color['l_oran'], hex(n)[2:], color['clean']))
else:
    print('{}OPÇÃO INVÁLIDA{}'.format(color['l_red'], color['clean']))
