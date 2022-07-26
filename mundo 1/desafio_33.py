a = int(input('Digite um numero: '))
b = int(input('Digite um numero: '))
c = int(input('Digite um numero: '))
maior = c
if a > b > c:
    maior = a
elif b > a > c:
    maior = b
print('O maior é {}'.format(maior))

menor = b
if a < c < b:
    menor = a
elif c < a < b:
    menor = c
print('O menor é {}'.format(menor))

