arquivo = []
while True:
    nome = str(input('Nome: ')).strip().title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    arquivo.append([nome, [nota1, nota2], media])
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if perg == 'N':
        break

print('=-'*50)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*50)
for c, v in enumerate(arquivo):
    print(f'{c:<4}{v[0]:<10}{v[2]:>8.1f}')

while True:
    print('-'*30)
    perg2 = int(input('Mostrar nostas de qual aluno? [999 interrompe]: '))
    if perg2 == 999:
        break
    if 0 <= perg2 <= len(arquivo)-1:
        print(f'Notas de {arquivo[perg2][0]} são {arquivo[perg2][1]}')
