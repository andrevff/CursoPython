l1 = float(input('Primeiro lado do triângulo: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceito lado: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Esses segmentos podem formar um triangulo!')
else:
    print('Esses segmentos não podem formar um triangulo :(')
