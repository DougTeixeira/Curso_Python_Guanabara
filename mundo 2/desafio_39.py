idade = int(input('\033[1;31mDigite sua idade:\033[m '))

if idade < 18:
    print('\033[0;33mVocê ainda ira se alistar, faltam ainda {} anos para você se apresentar.'.format(18-idade))
elif idade == 18:
    print('\033[1;33mEstá na hora de você se alistar.')
elif idade > 18:
    print('\033[1;35mSeu tempo de alistamento ja passou, você está atrasado a {} anos,' \
          'vá se apresentar.'.format(idade - 18))
else:
    print('Idade invalida')