dis = float(input('Digite a distância da viagem em Km: '))
if dis <= 200:
    valor = dis * 0.5
    print('Valor da viagem: R$ {:.2f}'.format(valor))
else:
    valor = dis * 0.45
    print('Valor da viagem: R$ {:.2f}'.format(valor))
