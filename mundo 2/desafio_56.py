soma = 0
maior = 0
nome_m = ''
mulher_20 = 0
for i in range(1, 5):
    print('-' * 5, '{}° pessoa'.format(i),'-'*5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma += idade
    if i == 1 and sexo in 'Mm':
        maior = idade
        nome_m = nome
    elif idade > maior and sexo in 'Mm':
        maior = idade
        nome_m = nome
    elif sexo in 'Ff' and idade < 20:
        mulher_20 += 1
media = soma/4
print('A média de idade do grupo é de {:.0f} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior, nome_m))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulher_20))