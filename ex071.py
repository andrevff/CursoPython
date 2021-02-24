print('='*30)
print('CAIXA ELETRÔNICO'.center(27))
print('='*30)
valor = int(input('Quanto deseja sacar? R$'))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced +=1
    else:
        print(f'{totalced} de R${ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced =1
        totalced = 0
        if total == 0:
            break
