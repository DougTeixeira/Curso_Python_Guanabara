primeiro_n = int(input('Digite o primeiro valor: '))
segundo_n = int(input('Digite o segundo valor: '))

if primeiro_n > segundo_n:
    print('O primeiro valor {}, é maior!'.format(primeiro_n))
elif primeiro_n < segundo_n:
    print('O segundo valor {}, é maior!'.format(segundo_n))
else:
    print('Não existe valor maior, os dois são iguais.')