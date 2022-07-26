import moeda109

p = float(input('Digite o preço: '))
print(f'A metade de {moeda109.moeda(p)} é {moeda109.metade(p)}')
print(f'O dobro de {moeda109.moeda(p)} é {moeda109.dobro(p, True)}')
print(f' Aumentando 10% temos {moeda109.aumentar(p, 10, False)}')
print(f' Diminuindo 20% temos {moeda109.diminuir(p, 20, True)}')