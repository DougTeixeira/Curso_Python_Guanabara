nota_1 = float(input('Digite sua primeira nota: '))
nota_2 = float(input('Digite sua segunda nota: '))

if (nota_1 + nota_2)/2 < 5.0:
    print('\033[1:31mREPROVADO')
elif 7 > (nota_1 + nota_2)/2 >= 5.0:
    print('\033[1:33mRECUPERAÇÃO')
elif 10.0 > (nota_1 + nota_2)/2 >= 6.9:
    print('\033[1:34mAPROVADO')
else:
    print('Alguma nota está invalida.')
