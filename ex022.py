nome = str(input('Digite o seu nome: '))
print('Nome com letras maiúsculas: {}'.format(nome.upper()))
print('Nome com letras minúsculas: {}'.format(nome.lower()))
print('Quantidade de letras: {}'.format(len(nome) - nome.count(' ')))
nome1 = nome.split()
print('Quantidade de letras do primeiro nome: {}'.format(len(nome1[0])))