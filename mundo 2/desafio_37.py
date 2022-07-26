num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases
[1] BINÁRIAO
[2] OCTAL
[3] HEXADECIMAL''')

opção = int(input('Sua opção: '))

if opção == 1:
    print('{} convertido para binario é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para otal é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida')
