from random import shuffle # shufle embaralha os valores
lista = []

for i in range(1, 5):
    item = input('deseja inserir:')
    lista.append(item)

shuffle(lista)
print(lista)
