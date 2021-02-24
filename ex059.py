op = 0
while op != 5:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    print("""---- M E N U ----
1 - Somar
2 - Multiplicar
3 - Maior
4 - Novos Números
5 - Sair do programa""")
    print('-'*20)
    op = int(input('Digite a opção: '))
    if op == 1:
        soma = n1 + n2
        print('---- Soma: ')
        print('{} + {} = {}'.format(n1, n2, soma))
        print('-'*20)
    elif op == 2:
        mult = n1 * n2
        print('---- Multiplicação: ')
        print('{} X {} = {}'.format(n1, n2, mult))
        print('-'*20)
    elif op == 3:
        if n1 > n2:
            print('{} é maior que {}. '.format(n1, n2))
        elif n2 > n1:
            print('{} é maior que {}. '.format(n2, n1))
        else:
            print('Os números são iguais!')
    elif op == 4:
        print('Escolha novos números!')
    elif op == 5:
        print('Encerrando...')
    else:
        print('Opção Inválida! Reiniciando...')
