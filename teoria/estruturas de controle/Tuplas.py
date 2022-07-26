lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')

# for comida in lanche:
#     print(f'Eu vou comer {comida}')
#
# for count in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[count]} na posição {count}')
#
# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos}.')
#
# print('Comi pra caramba.')


# print(sorted(lanche)) # ordenar os itens


# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = a + b # vai criar uma nova tupla com a tupla A dps a tupla B, a + b != b + a
# print(c)
# print(len(c))
# print(c.count(5)) # conta quantas vezes o numero 5 aparece na tupla C
# print(c.index(2)) # pega o indice da primeira ocorrencia do objeto escolhido
# print(c.index(5,1)) # pega o indice da primeira ocrrencia do objeto escolhido a partir do indice escolhido


pessoa = ('Douglas', 23, 'M')
del(pessoa) #so se pode deletar a tupla, não altera-la.
print(pessoa)