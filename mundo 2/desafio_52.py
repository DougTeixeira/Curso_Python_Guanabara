num = int(input('Digite um numero: '))
soma = 0

for i in range(1, num +1):
    if num % i == 0:
        print('\033[34m', end='')
        soma += 1
    else:
        print('\033[31m', end='')
    print(i, end=' ')

print('\n\033[35mO numero {}, foi divisivel {} vezes.\033[m'.format(num, soma))

if soma == 2:
    print('\033[34mO numero {} é primo.'.format(num))
else:
    print('\033[31mO numero {} não é primo.'.format(num))