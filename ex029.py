vel = float(input('Informe a velocidade do carro: '))
if vel > 80:
    print('Você foi multado!')
    multa = (vel - 80) * 7
    print('Valor da multa: R$ {:.2f}'.format(multa))
else:
    print('Não consta nenhuma multa')
