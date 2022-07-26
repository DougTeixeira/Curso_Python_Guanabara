soma = count = 0
while True:
    valor = int(input('Digite um valor [digite 999 para parar]: '))
    if valor == 999:
        break
    else:
        soma += valor
        count += 1
print('Vc digitou {} números e a soma entre eles é {}.'.format(count, soma))