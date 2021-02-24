from random import randint
pc = randint(0, 10)
n = 11
c = 1
print('O computador pensou em um número. Tente adivinhar qual foi!')
while n != pc:
    n = int(input('Digite: '))
    if n != pc:
        print('Errado! Tente novamente.')
        c += 1
    else:
        print('Parabéns! Você acertou depois de {} tentativas.'.format(c))
print('O número foi o {}'.format(pc))
