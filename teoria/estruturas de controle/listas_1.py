# num = [2, 5, 9 ,1]
# num[2] = 3 # substitui oq tem no indice 2, pelo valor 3
# num.append(7) # adiciona ao final da lista o valor 7
# num.sort() # coloca em ordem
# num.sort(reverse=True) # coloca em ordem reversa
# num.insert(2, 0) # vai inserir no indice 2, o valor 0 sem eliminar ou substituir nada
# num.pop() # vai eliminar o ultimo valor
# num.pop(2) # vai eliminar o valor do indice 2
# num.remove(2) # remove o primeiro elemento 2
#
# if 4 in num:
#     num.remove(4)
# else:
#     print('Não ahcei o numero 4')
#
# print(f'Essa lista tem {len(num)} elementos.') # tamanho da lista
# print(num)


# valores = []
# for count in range(0, 3):
#     valores.append(int(input('Digite um valor: ')))
#
# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}.')


# a = [2, 3, 4, 7]
# b = a # isso cria uma ligação entre B e A, se mudar algo em B ou em A, mudara na outra tbm
# a[1] = 2
# print(a)
# print(b)

# a = [2, 3, 4, 7]
# b = a[:] # isso cria uma copia de A para o B, assim, não tendo uma ligação, mudando individualmente cada uma
# a[1] = 2
# print(a)
# print(b)