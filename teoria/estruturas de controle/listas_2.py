# teste = list()
# teste.append('Douglas')
# teste.append(23)
# galera = []
# galera.append(teste) # cria uma ligação
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste) # colocou a ligação de novo
# print(teste) # ['Maria', 22]
# print(galera) # [['Maria', 22], ['Maria', 22]]

# teste = list()
# teste.append('Douglas')
# teste.append(23)
# galera = []
# galera.append(teste[:]) # cria uma copia de teste
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:]) # colocou uma copia do novo teste
# print(teste) # ['Maria', 22]
# print(galera) # [['Douglas', 23], ['Maria', 22]]


# galera = [['João', 23], ['Maria', 40], ['Caio', 15]]
# print(galera[2][1]) # 15
# # for i in galera:
# #     print(i)
# #     ['João', 23]
# #     ['Maria', 40]
# #     ['Caio', 15]


# galera = [['João', 23], ['Maria', 40], ['Caio', 15]]
# for i in galera:
#     print(i[0])
#     João
#     Maria
#     Caio


# galera = [['João', 23], ['Maria', 40], ['Caio', 15]]
# for i in galera:
#     print(i[1])
#     23
#     40
#     15


# galera = [['João', 23], ['Maria', 40], ['Caio', 15]]
# for i in galera:
#     print(f'{i[0]} tem {i[1]} anos de idade.')


galera = list()
dado = list()
totmai = totmen = 0
for i in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] > 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')

# somar um conteudo da lista
# sun(nome da lista)
#lista_produto = ['ipone', 'mac', 'aple', 'ipad']
#lista_preco = [5000, 9000, 2500, 7000]
# for produto, preco in zip(lista_produto, lista_preco):
#    print(f'Produto {produto} custa: R${preco}')
