idade = int(input('Digite a sua idade: '))
if idade < 18:
    print('Você ainda não pode se alistar, mas faltam {} anos'.format(18 - idade))
elif idade == 18:
    print('Você deve se alistar ainda esse ano.')
else:
    print('Você já deveria ter se alistado a {} anos'.format(idade -18))
