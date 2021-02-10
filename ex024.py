city = str(input('Digite o nome de uma cidade: '))
city1 = city.split()
print('O nome começa com Santo? {}'.format(city1[0].lower().find('santo')))
