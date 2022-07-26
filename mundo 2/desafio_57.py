sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('Sexo invalido, por favor, digite seu sexo novamente [M/F]: ')\
               ).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))