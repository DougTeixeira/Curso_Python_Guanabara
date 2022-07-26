galera = []
dado = list()
mai = men = 0

while True:
    dado.append(str(input('Digite um nome: ')))
    dado.append(int(input('Digite o peso: ')))
    if len(galera) == 0:
        mai = men = dado[1]
    else:
        if mai < dado[1]:
            mai = dado[1]
        if men > dado[1]:
            men = dado[1]
    galera.append(dado[:])
    dado.clear()
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
    if perg == 'N':
        break

print(f'Ao todo você cadastrou {len(galera)} pessoas.')
print(f'O maior peso foi de {mai:.1f} Kg. O peso é de', end=' ')
for x in galera:
    if x[1] == mai:
        print(f'[{x[0]}]', end=' ')
print(f'\nO menor peso foi de {men:.1f} Kg. O peso é de', end=' ' )
for y in galera:
    if y[1] == men:
        print(f'[{y[0]}]', end=' ')