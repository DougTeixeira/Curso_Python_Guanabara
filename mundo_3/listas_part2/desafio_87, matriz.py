#para matrizes maiores de 3 x 3
matriz = []
temp = []
soma_par = soma_terc = maior_seg = 0
perg1 = int(input('Digite o numero de linhas: '))
perg2 = int(input('Digite o numero de colunas: '))
for l in range(0, perg1):
    for c in range(0, perg2):
        temp.append(int(input(f'Digite o valor de [{l}, {c}]: ')))
    matriz.append(temp[:])
    temp.clear()
for l in range(0, perg1):
    for c in range(0, perg2):
        print(f'[{matriz[l][c]}]', end='')
    print()

for l in range(0, perg1):
    for c in range(0, perg2):
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]

        if matriz[l][c] == matriz[l][2]:
            soma_terc += matriz[l][c]

        if matriz[l][c] == matriz[1][1]:
            maior_seg = matriz[l][c]

        else:
            if maior_seg < matriz[1][c]:
                maior_seg = matriz[l][c]

print(f'A soma dos valore pares é {soma_par}')
print(f'A soma dos valores da terceira coluna é {soma_terc}')
print(f'O maior valor da segunda linha é {maior_seg}')

