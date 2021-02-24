print('---- SEQUÊNCIA DE FIBONACCI ----')
n = int(input('Digite um número: '))
c = 1
s1 = 0
s2 = 1
print(s1, end=' → ')
print(s2, end=' → ')
while c <= (n-2):
    s3 = s1 + s2
    print(s3, end=' → ')
    s1 = s2
    s2 = s3
    c +=1
