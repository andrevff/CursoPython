from random import randint
c = 0
print('='*30)
print('PAR OU IMPAR'.center(27))
print('='*30)
while True:
    n = int(input('Digite um valor de 0 a 10: '))
    op = str(input('Par ou ímpar? [P/I]: '))
    print('-'*30)
    pc = randint(0, 10)
    s = n + pc
    if op in 'Pp':
        if s % 2 == 0:
            print(f'Você jogou {n} e o PC {pc}. O total foi {s} e deu PAR.')
            print('-'*30)
            print('Você venceu! ')
            print('Vamos jogar novamente...')
            c += 1
        else:
            print(f'Você jogou {n} e o PC {pc}. O total foi {s} e deu ÍMPAR.')
            print('-'*30)
            print('Você perdeu!')
            break
    if op in 'Ii':
        if s % 2 != 0:
            print(f'Você jogou {n} e o PC {pc}. O total foi {s} e deu ÍMPAR.')
            print('-' * 30)
            print('Você venceu! ')
            print('Vamos jogar novamente...')
            c += 1
        else:
            print(f'Você jogou {n} e o PC {pc}. O total foi {s} e deu PAR.')
            print('-' * 30)
            print('Você perdeu!')
            break
print('='*30)
print('GAME OVER'.center(27))
print('='*30)
print(f'Você venceu {c} vezes.')
