import moeda107

p = float(input('Digite o preço: '))
print(f'A metade de R${p} é R${moeda107.metade(p)}')
print(f'O dobro de R${p} é R${moeda107.dobro(p)}')
print(f' Aumentando 10% temos R${moeda107.aumentar(p, 10)}')
print(f' Diminuindo 20% temos R${moeda107.diminuir(p, 20)}')