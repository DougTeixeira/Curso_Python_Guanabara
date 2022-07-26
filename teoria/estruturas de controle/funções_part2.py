# help() #no terminal

# # help()
# help(print) # informações sobre oq escolher
#
# # print(.__doc__)
# print(input.__doc__) #informações sobre oq escolher

# docstrings
#implementando uma descrição no help para uma função que eu criei
#a linha a baixo de def é a docstrings
# abrir 3 aspas duplas e escrever:

# def contador(i, f, p):
#     """
#     -> Faz uma contagem e mostra na tela.
#     :param i: início da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     Função criada por Douglas
#     """
#     c = i
#     while c <= f:
#         print(f'{c}', end='..')
#         c += p
#     print('FIM')
#
# contador(1, 10,1)
# help(contador)


# Parametros opcionais
# def somar(a=0, b=0, c=0):
#     """
#     -> Faz a soma de três valores e mostra o resultado na tela.
#     :param a: o primeiro valor
#     :param b: o segundo valor
#     :param c: o terceiro valor
#     Função criada por Douglas
#     """
#     s = a + b + c
#     print(f'A soma vale {s}')
#
# somar(3, 2, 5)
# somar(8, 4)
# somar()
# help(somar)


# # Escopo de variáveis
# def teste():
#     x = 8 # variavel local
#     print(f'no programa teste n vale {n}')
#     print(f'na função teste x vale {x}')
# # programa principal
# n = 2 # variavel local
# print(f'no programa principal n vale {n}')
# teste()
# print(f'no programa princial x vale {x}')

# def função():
#     n1 = 4 # variavel local
#     print(f'N1 dentro vale {n1}')
#
# n1 = 2 variavel global
# função()
# print(f'N1 fora vale {n1}')


# def função():
#     global n1 # muda a variavel global ja por uma local, virando a nova global
#     n1 = 4
#     print(f'N1 dentro vale {n1}')
#
# n1 = 2
# função()
# print(f'N1 fora vale {n1}')


# # RETORNO DE VALORES
# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     return s
# r1 = somar(3, 5, 2)
# r2 = somar(5, 2)
# r3 = somar(6)
# print(f'Os resultados foram {r1}, {r2} e {r3}')

# def fatorial(num=1):
#     f = 1
#     for i in range(num, 0, -1):
#         f *= i
#     return f
# n = int(input('Digite um numero: '))
# print(f'O fatorial de {n} é {fatorial(n)}.')

def par(n=0):
    if n % 2 ==0:
        return True
    else:
        return False
num = int(input('Digite um numero: '))
print(par(num))
if par(num):
    print('É par')
else:
    print('Não é par')