from datetime import date
atual = date.today().year
total_maior= 0
total_menor = 0
for i in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(i)))
    idade = atual - nasc
    if idade >= 21:
        total_menor += 1
    else:
        total_maior += 1
print('Ao todo, temos {} maiores de idade'.format(total_maior))
print('Ao todo, temos {} menores de idade'.format(total_menor))
