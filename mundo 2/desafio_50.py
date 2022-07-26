soma = 0
count = 0
for i in range(1,7):
    i = int(input('Digite um numero: '))
    if i % 2 == 0:
        soma += i
        count += 1

print('Vc informou {} numeros pares, a soma deles é {}.'.format(count, soma))