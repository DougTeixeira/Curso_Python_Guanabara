from random import randint
from time import sleep

def sorteia(lista):
    print('SORTEANDO 5 VALORES PARA A LISTA: ', end='')
    for i in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.5)
    print('PRONTO')
    sleep(0.5)

def somapar(lista):
    soma = 0
    print('OS VALORES PARES SÃO: ', end='')
    sleep(0.5)
    for i in lista:
        if i % 2 == 0:
            soma += i
            print(i, end=' ', flush=True)
            sleep(0.5)
    print(f'\nA SOMA DOS VALORES PARES É: {soma}')

numeros = []

sorteia(numeros)
somapar(numeros)