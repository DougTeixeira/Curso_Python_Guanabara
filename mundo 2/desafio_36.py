print('\033[1;31;40m-*-\033[m'*20)
print(' '*18, '\033[1;31;40mPrograma de Emprestimo\033[m')
print('\033[1;31;40m-*-\033[m'*20)

casa = float(input('\033[1;33mDigite o valor da casa: '))
salario = float(input('\033[1;34mDigite o valor do seu salario: '))
anos = float(input('\033[1;35mDigite em quantos anos você ira pagar: '))

prestação = casa / (anos * 12)

if prestação <= salario * 0.3:
    print('O valor da parcela mensal será de R${: .2f}, para ser paga em {: .0f} meses'.format(prestação, anos*12))
else:
    print('Infelizmente, a prestação de R${: .2f} nesse determinado tempo de {: .0f}, '\
          'ultrapassa 30% do seu salario.'.format(prestação, anos * 12))