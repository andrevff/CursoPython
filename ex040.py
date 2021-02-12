n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Média: {:.1f}'.format(m))
if m < 5:
    print('REPROVADO')
elif 5 <= m < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
