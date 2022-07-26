frase = 'Curso em Video Python'

#Fatiamento
print(frase[9:21:2])

#Contar quantas vezes existe a letra o
print(frase.count('o'))

#Contar o tamanho da variavel
print(len(frase))

#Contar quantas vezes existe a letra o, entre os indices 0 e 13.
print(frase.count('o', 0, 13))

#mostrar em qual indice começa 'deo'
print(frase.find('deo'))

#Indice do ultimo 'a' na frase
print(frase.rfind('a'))

#vai retornar -1, que significa q n existe na frase
print(frase.find('android'))

#Retorna verdadeiro ou falso, caso exista a str dentro da variavel
print('Curso' in frase)

#Troca a palavra python por android apenas na hora de printar
print(frase.replace('Python', 'Android'))
print(frase)

#Trocar uma palavra na str e salvar
frase2 = frase.replace('Python', 'Android')
print(frase2)

# Colocar tudo em maiusculo
print(frase.upper())


# Colocar tudo em minusculo
print(frase.lower())

#Transforma tudo em minusculo e muda a primeira letra da frase para maiuscula
print(frase.capitalize())

#Transforma tudo em minusculo e muda a primeira letra de cada palavra para maiuscula
print(frase.title())

frase1 ='    Aprender Python     '
print(frase1)
#Remove os espaços antes e depois das palavras
print(frase1.strip())

#Tirar os espaços da direita
print(frase1.rstrip())

#Tirar os espaços da esquerda
print(frase1.lstrip())

#Separou cada palavra para ser um item de uma lista.
print(frase.split())
print(frase.split(' '))

#Separar a frase em uma lista com split, e usar o .join para juntar com '-'
# frase = frase.split(' ')
# print('-'.join(frase))
print('-'.join(frase.split(' ')))

# print('{:^50}'.format('JOGO DA MEGA SENA')) # centralizar o print
# print(f'{"JOGO DA MEGA SENA":^30}') # centralizar o print

print('=-'*50)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*50)

print('OLA, SOU O DOUGLAS, TUDO BOM.'.replace(',','.'))
# replace substitui o primeiro parametro pelo segundo.

print('OI'.center(42))