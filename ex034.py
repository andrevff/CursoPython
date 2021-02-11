sal = float(input('Digite o salário do funcionário: '))
if sal > 1250:
    novo = (sal * (10/100)) + sal
    print('Novo salário com 10% de aumento: R$ {:.2f}'.format(novo))
else:
    novo = (sal * (15/100)) + sal
    print('Novo salário com 15% de aumento: R$ {:.2f}'.format(novo))
