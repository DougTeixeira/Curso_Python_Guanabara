pessoas = {'Nome': 'Douglas', 'Sexo': 'M', 'idade': 22}
# print(f'O {pessoas["Nome"]} tem {pessoas["idade"]} anos.')
# print(pessoas.values())
# print(pessoas.keys())
# print(pessoas.items())

# for k in pessoas.keys():
#     print(k)
#
# for v in pessoas.values():
#     print(v)
#
# for k, v in pessoas.items():
#     print(f'{k} = {v}')

# pessoas['Nome'] = 'Leandro'
# pessoas['Peso'] = 89
# del pessoas['Sexo']
# print(pessoas)

# brasil = []
# estado1 = {'uf': 'Ceará', 'sigla': 'CE'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(estado1)
# print(estado2)
# print(brasil)
# print(brasil[0]['uf'])
# print(brasil[1]['sigla'])

# brasil.append(estado.copy())    # copiar um dicionario para uma lista

estado = dict()
brasil = list()
for i in range(0, 2):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for l in brasil:
    for k, v in l.items():
        print(f'O campo {k} tem valor {v}')
    for k in l.keys():
        print(k, end=' ')
    print()
    for v in l.values():
        print(v, end=' ')
    print()