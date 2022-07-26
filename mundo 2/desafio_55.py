maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input('O peso da {}° pessoa é: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print('O maior peso lido foi de {} kg.'.format(maior))
print('O menor peso lido foi de {} kg.'.format(menor))