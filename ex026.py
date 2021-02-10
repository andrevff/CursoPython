frase = str(input('Digite uma frase: ')).strip()
print('Quantidade de letras A que aparecem: {}'.format(frase.lower().count('a')))
print('Posição em que aparece pela primeira vez: {}'.format(frase.lower().find('a')+1))
print('Posição em que aparece pela última vez: {}'.format(frase.lower().rfind('a')+1))
