#Voce errou
from random import randint
import playsound
nome = input('Digite seu nome: ')
num = int(input('Digite um número de 0 a 5 : '))
r = str(randint(0,5))
if num == r:
    print('Parabéns seu sortudo, você acertou!!')
else:
    print('Você errou! O número que eu escolhi foi {}'.format(r))
    playsound.playsound('ex028.mp3')
print('Foi bom jogar com você {}'.format(nome))
