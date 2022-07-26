from random import choice
from time import sleep

numero_secreto = choice(range(0, 6))

print('=-='*20)
print('Tente adivinhar')
print('=-='*20)

numero = int(input('Digite um número: '))
print('Processando...')
sleep(3)

if numero_secreto == numero:
    print('Você acertou, número é {}'.format(numero_secreto))

else:
    print('Você errou, o número correto é {}'.format(numero_secreto))

