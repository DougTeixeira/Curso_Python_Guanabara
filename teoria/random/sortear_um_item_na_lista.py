from random import choice
lista = []

for i in range(1, 5):
    item = input('deseja inserir:')
    lista.append(item)


print(choice(lista))
