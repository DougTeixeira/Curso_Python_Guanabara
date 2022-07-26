from random import randint
from time import sleep
from operator import itemgetter
jogo = {}

jogo['Jogador1'] = randint(1, 6)
jogo['Jogador2'] = randint(1, 6)
jogo['Jogador3'] = randint(1, 6)
jogo['Jogador4'] = randint(1, 6)
ranking = list()
print('-='*50)
print('       VALORES SORTEADOS')
for k, v in jogo.items():
    print(f'    {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# key=itemgetter(1) ordena de acordo com os valores sorteados,
# se fosse key=itemgetter(0) ordenava de acordo com os números dos jogadores
print('   == RANKING DOS JOGADORES ==   ')
for k, v in enumerate(ranking):
    print(f'    {k+1}° lugar: {v[0]} com {v[1]}')
    sleep(1)