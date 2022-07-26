lista = []
dados = {}
soma_idade = 0
while True:
    dados['nome'] = str(input('Nome: ')).strip().title()
    dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while dados['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    dados['idade'] = int(input('Idade: '))
    soma_idade += dados['idade']
    lista.append(dados.copy())
    dados.clear()

    perg = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while perg not in 'SN':
        print('ERRO! Por favor, digite apenas S ou N.')
        perg = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if perg == 'N':
        break
print('-=' * 40)

if len(lista) == 1:
    print(f'A) Ao todo temos {len(lista)} pessoa cadastrada.')
else:
    print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')

media = soma_idade / len(lista)
print(f'B) A média de idade é {media:.2f}')

print(f'C) As mulheres cadastradas foram: ', end='')
for l in lista:
    if l['sexo'] == 'F':
        print(f'[{l["nome"]}]', end=' ')
print()

print(f'D) Lista das pessoas que estão acima da média:')
for p in lista:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
        print()

print('<< ENCERRADO >>')
