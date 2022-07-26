salario = int(input('Digite o valor do salario: '))

if salario > 1250:
    aumento = salario * 1.1
    print('O aumento de 10% é {: .2f}'.format(aumento))

else:
    aumento = salario * 1.15
    print('O aumento de 10% é {: .2f}'.format(aumento))
