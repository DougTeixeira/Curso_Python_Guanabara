valores = []
pares = []
impares = []
while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if perg == 'N':
        break
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')