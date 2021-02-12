color = {
    'clean': '\033[m',
    'b_blue': '\033[44m',
    'l_blue': '\033[34m',
    'l_green': '\033[32m',
    'l_red': '\033[31m'
}
print('{}={}'.format(color['b_blue'], color['clean'])*20)
print('{}Empréstimo{}'.format(color['l_blue'], color['clean']).center(27))
print('{}={}'.format(color['b_blue'], color['clean'])*20)
casa = float(input('Informe o valor da casa: '))
sal = float(input('Informe o seu salário: '))
anos = float(input('Informe em quantos anos deseja pagar: '))
pres = casa / (anos*12)
i = sal*(30/100)
if pres <= i:
    print('='*20)
    print('{}EMPRÉSTIMO APROVADO{}'.format(color['l_green'], color['clean']))
    print('Você pagará {}R$ {:.2f}{} por mês.'.format(color['l_blue'], pres, color['clean']))
else:
    print('='*20)
    print('{}EMPRÉSTIMO NEGADO{}'.format(color['l_red'], color['l_red']))
