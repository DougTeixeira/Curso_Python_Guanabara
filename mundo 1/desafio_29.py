from time import sleep
vel_carro = float(input('Qual a velocidade do carro? '))
print('Aguarde enquanto faço os calculos...')
sleep(2)

if vel_carro >= 80:
    valor = (vel_carro-80)*7
    print('Você foi multado, pois está com uma velocidade de {},\n'
          'terá que pagar uma multa de {} reais'.format(vel_carro, valor))
else:
    print('Você está de acordo com a lei, pois está com uma velocidade de {}'.format(vel_carro))
