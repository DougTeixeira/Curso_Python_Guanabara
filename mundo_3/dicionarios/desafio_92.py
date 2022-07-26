from datetime import datetime
pessoa = {}

pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = datetime.now().year - int(input('Ano de nascimento: '))
pessoa['carteira'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['carteira'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salario'] = int(input('Salario: R$'))
    pessoa['aposentadoria'] = pessoa['contratação'] + 35 + pessoa['idade'] - datetime.now().year
else:
    pessoa['contratação'] = 'Não tem carteira de trabalho.'
print('-='*40)

for k, v in pessoa.items():
    print(f'{k}: {v}')