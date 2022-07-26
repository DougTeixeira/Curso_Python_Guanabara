valores = []
while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    perg = ' '
    while perg not in 'SsNn':
        perg = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
    if perg == 'N':
        break
print(f'Foram digitados {len(valores)}')
valores.sort(reverse=True)
print(f'A lista de valores ordenada de forma decrescente é: {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')