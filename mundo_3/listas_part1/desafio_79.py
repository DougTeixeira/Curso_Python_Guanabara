valores = []
while True:
    valor = (int(input('Digite um valor: ')))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não irei adicionar...')

    perg = ' '
    if perg not in 'SN':
        perg = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if perg == 'N':
        break
valores.sort(valores)
print(f'Você adicionou os valores {valores}')