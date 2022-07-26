grupo = [[], []]
for i in range(1, 8):
    valor = int(input(f'Digite o {i}° valor: '))
    if valor % 2 == 0:
        grupo[0].append(valor)
    else:
        grupo[1].append(valor)
grupo[0].sort()
grupo[1].sort()
print('=-'*30)
print(f'Os valores pares digitados foram: {grupo[0]}')
print(f'Os valores impares digitados foram: {grupo[1]}')