print('='*30)
print('LOJA SUPER BARATÃO')
print('='*30)

total = tot1000 = menor = count = 0
nome_menor = ''
while True:
    nome = str(input('Nome do produto: ')).strip()
    preço = int(input('Preço: R$'))
    total += preço
    count += 1
    if preço >= 1000:
        tot1000 += 1
    if count == 1 or preço < menor:
        menor = preço
        nome_menor = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total de compras foi de {total:.2f}')
print('Temos {} produtos custando mais de R$ 1000.00'.format(tot1000))
print('O produto mais barato foi de {} que custa R$ {}.'.format(nome, menor))