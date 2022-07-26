soma = 0
count = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        count += 1
print('A soma dos {} numeros é {}.'.format(count, soma))