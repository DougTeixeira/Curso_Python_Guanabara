aluno = {}
print('=*='*50)
aluno['nome'] = str(input('Nome: '))
while True:
    aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
    if 10 >= aluno['média'] >= 7:
        aluno['situação'] = 'Aprovado'
        break
    elif 7 > aluno['média'] >= 5:
        aluno['situação'] = 'Recuperação'
        break
    elif 5 > aluno['média'] >= 0:
        aluno['situação'] = 'Reprovado'
        break
    else:
        print('O valor digitado é invalido!')
print('=*='*30)
print(f'{"Sobre o aluno(a):":>20} {aluno["nome"]}')
print(f'{"Média é igual a":>20} {aluno["média"]}')
print(f'{"Situação é igual a":>20} {aluno["situação"]}')