resp = 'S'
soma = count = media = maior = menor = 0
while resp == 'S':
    valor = int(input('Digite um numero: '))
    soma += valor
    count += 1
    resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if count == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor
media = soma/count
print('A média dos valores digitados é {}.'.format(media))
print('O maior valor {} e o menor valor {}.'.format(maior, menor))
