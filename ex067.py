n = 0
while True:
    print('-' * 40)
    n = int(input('Quer ver a tabuada de qual número? '))
    print('-' * 40)
    if n < 0:
        break
    for c in range(1, 11):
        mult = n * c
        print(f'{n} X {c} = {mult}')
print('Encerrando...')
