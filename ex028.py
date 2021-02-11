import random

n1 = random.randint(0, 5)
n2 = int(input('Digite um número: '))
if n1 == n2:
    print('Parabéns, você acertou!')
else:
    print('Você errou! O número certo seria o {}'.format(n1))
