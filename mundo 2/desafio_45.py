from random import choice, randint
from time import sleep

jogo = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)

print('\033[1;32;40m-=\033[m'*30)
print(' '*15, '\033[1;31;40mVAI COMEÇAR O COMBATE!!!\033[m')
print('\033[1;32;40m-=\033[m'*30)

jogador = int(input('''\033[1;31;40mDentre as opções:\033[m'
\033[1;31;40m[1] pedra\033[m
\033[1;31;40m[2] papel\033[m
\033[1;31;40m[3] tesoura\033[m
\033[1;33;40mEscolha um:\033[m '''))

print('\033[4;35;40mJO\033[m')
sleep(1)
print('\033[4;35;40mKEN\033[m')
sleep(1)
print('\033[4;35;40mPO!!!\033[m')

print('\033[1;34;40m*-*\033[m'*15)
print(' '*9, '\033[1;31;40mComputador jogou {}!!!\033[m'.format(jogo[computador]))
print(' '*11, '\033[1;31;40mJogador jogou {}!!!\033[m'.format(jogo[jogador]))
print('\033[1;34;40m*-*\033[m'*15)

if computador == 0:
    if jogador == 0:
        print(' '*15,'\033[1;31;40mEmpate\033[m')
    elif jogador == 1:
        print(' '*15,'\033[1;31;40mVocê venceu\033[m')
    elif jogador == 2:
        print(' '*15,
              '\033[1;31;40mVocê perdeu\033[m')
    else:
        print(' '*15,
              '\033[1;31;40mJogada invalida!\033[m')
elif computador == 1:
    if jogador == 0:
        print(' '*15,
              '\033[1;31;40mVocê perdeu\033[m')
    elif jogador == 1:
        print(' '*15,
              '\033[1;31;40mEmpate\033[m')
    elif jogador == 2:
        print(' '*15,
              '\033[1;31;40mVocê venceu\033[m')
    else:
        print(' '*15,
              '\033[1;31;40mJogada invalida!\033[m')
elif computador == 2:
    if jogador == 0:
        print(' '*15,
              '\033[1;31;40mVocê venceu\033[m')
    elif jogador == 1:
        print(' '*15,
              '\033[1;31;40mVocê perdeu\033[m')
    elif jogador == 2:
        print(' '*15,
              '\033[1;31;40mEmpate\033[m')
    else:
        print(' '*15,
              '\033[1;31;40mJogada invalida!\033[m')