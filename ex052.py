cont = 0
n = int(input("Digite um número inteiro: "))
for c in range(2, n):
    if n % c == 0:
        cont = cont + 1
if cont == 0:
    print('PRIMO')
else:
    print('NÃO É PRIMO')
