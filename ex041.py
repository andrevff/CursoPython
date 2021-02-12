idade = int(input('Digite a idade do atleta: '))
if idade <= 9:
    print('CATEGORIA: Mirim')
elif 10 <= idade <= 14:
    print('CATEGORIA: Infantil')
elif 15 <= idade <= 19:
    print('CATEGORIA: Júnior')
elif idade <= 20:
    print('CATEGORIA: Sênior')
else:
    print('CATEGORIA: Master')
