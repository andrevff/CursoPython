c = 0
mai18 = 0
homens = 0
men20 = 0
sexo = ' '
while True:
    print('='*30)
    print('CADASTRE UMA PESSOA'.center(27))
    print('='*30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: '))
    if idade >= 18:
        mai18 += 1
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: '))
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        men20 += 1
    print('-'*30)
    op = str(input('Deseja continuar? [S/N]: '))
    if op in 'Nn':
        break
print('-'*20)
print(f'Total de pessoas com mais de 18 anos: {mai18}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com menos de 20 anos: {men20}')
