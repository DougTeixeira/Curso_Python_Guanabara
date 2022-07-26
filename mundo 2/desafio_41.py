from datetime import date
atual = date.today().year
nascimento = float(input('Digite seu ano de nascimento: '))
idade = atual - nascimento

if idade <= 9:
    print('Vc participará da categoria, mirim.')
elif idade <= 14:
    print('Vc participará da categoria, infantil.')
elif idade <= 19:
    print('Vc participará da categoria, junior.')
elif idade <= 20:
    print('Vc participará da categoria, sénior.')
elif idade > 20:
    print('Vc participará da categoria, master.')
else:
    print('Idade invalida!')