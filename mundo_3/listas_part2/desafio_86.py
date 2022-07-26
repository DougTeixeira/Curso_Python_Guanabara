matriz = []
temp = []
count1 = count2 = 0
perg1 = int(input('Quantas linhas deseja? '))
perg2 = int(input('Quantas colunas deseja? '))

for x in (1, perg1):
    for i in range(0, perg2):
        temp.append(int(input(f'Digite um valor para [{count1},{i}]: ')))
    matriz.append(temp[:])
    temp.clear()
    count1 += 1
    print(x)

print(temp)
print(matriz)