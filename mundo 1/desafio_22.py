nome = str(input('Qual seu nome: ')).strip()

print('nome maiusculo: ', nome.upper())
print('nome minusculo: ', nome.lower())
print('total de letras sem espaço: ',len(''.join(nome.split(' '))))
print('tamanho do primeiro nome: ', len(nome.split(' ')[0]))
print('tamanho do primeiro nome: ',nome.find(' '))
