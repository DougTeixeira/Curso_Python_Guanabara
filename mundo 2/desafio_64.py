n = int(input('Digite um número [999 para parar]: '))
soma = count =0

while n != 999:
    soma += n
    count += 1
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(count, soma))