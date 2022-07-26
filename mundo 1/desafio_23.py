numero = str(input('Digite o numero entre 0 e 9999: ')).strip()

print('Unidade:{} \n'
      'Dezena: {} \n'
      'Centena {} \n'
      'Milhar {} \n'.format(numero[3], numero[2], numero[1], numero[0]))
