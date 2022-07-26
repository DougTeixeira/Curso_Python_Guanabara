from random import randint
from time import sleep
print('-'*30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('-'*30)

jogo = []
temp = []
perg = int(input('Quantos jogos você quer que eu sorteie? '))

for x in range(0, perg):
    while True:
        valor = randint(1, 60)
        if valor not in temp:
            temp.append(valor)
        if len(temp) == 6:
            break
    temp.sort()
    jogo.append(temp[:])
    temp.clear()

print(f'{f" SORTEANDO {perg} JOGOS ":=^30}')

for c, v in enumerate(jogo):
    print(f'Jogo {c+1}: {v}')
    sleep(1)
print('{:=^30}'.format('BOA SORTE'))