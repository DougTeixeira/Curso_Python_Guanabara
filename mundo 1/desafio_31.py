distancia = float(input('Qual a distancia da sua viagem? '))

# if distancia <= 200:
#     print('Para a distancia de', distancia)
#     valor = distancia * 0.5
#
# else:
#     print('Para a distancia de', distancia)
#     valor = distancia * 0.45
valor = distancia * 0.5 if distancia <= 200 else distancia * 0.45
print('O valor da viagem é R$ {: .2f}'.format(valor))
