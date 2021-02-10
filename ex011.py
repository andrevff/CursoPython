lar = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura em metros: '))
area = lar * alt
tinta = area / 2
print('A parede tem {:.2f}m² de área e serão necessários {:.2f}L de tinta para pintá-la'.format(area, tinta))
