num = str(input('Digite um número inteiro entre 0 e 9999: '))
num2 = num.rjust(4)
print('Unidade: {}'.format(num2[3]))
print('Dezena: {}'.format(num2[2]))
print('Centena: {}'.format(num2[1]))
print('Milhar: {}'.format(num2[0]))
