sexo = str(input('Digite o sexo de uma pesssoa[M/F]: '))
while sexo not in 'MmFf':
    print('Invalido, tente novamente')
    sexo = str(input('Digite o sexo de uma pesssoa[M/F]: '))
print('Fim')
