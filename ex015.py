dist = float(input('Digite quantos Km foram rodados: '))
dias = int(input('Quantos dias: '))
valor = (dias * 60) + (dist * 0.15)
print('Valor do aluguel: R${:.2f}'.format(valor))
