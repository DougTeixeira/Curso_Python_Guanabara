from random import randint
from time import sleep
from operator import itemgetter

while True:
    print(f'\033[1;31;40m{"=*"*31}{"="}\033[m')
    print(f'\033[1;31;40m{"JOGANDO OS DADOS":.>40}{"":.<23}\033[m')
    print(f'\033[1;31;40m{"=*"*31}{"="}\033[m')
    sleep(1)
    jogo = dict()
    for i in range(1, 5):
        jogo[f'{i}° Jogador'] = randint(1, 6)

    for k, v in jogo.items():
        print(f'\033[1;31;40m{f"O {k} tirou: {v}":>42}{"":<21}\033[m')
        sleep(1)

    print(f'\033[1;31;40m{"*="*31}{"*"}\033[m')
    print(f'\033[1;31;40m{"RANKING DOS JOGADORES":>>42}{"":<<21}\033[m')
    sleep(1)
    ranking = list()
    ranking = (sorted(jogo.items(), key=itemgetter(1), reverse=1))

    for c, v in enumerate(ranking):
        print(f'\033[1;31;40m{f"O {c+1}° lugar é do {v[0]} que tirou: {v[1]}":>51}{"":<12}\033[m')
        sleep(1)

    print(f'{"OBRIGADO POR JOGAR":>40}')
    sleep(1)
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Jogar novamente? [S/N]: ')).strip().upper()[0]
    if perg == 'N':
        break