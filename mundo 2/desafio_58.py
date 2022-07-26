from random import randint

print('Sou seu computador...\n')
valor_secreto = randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10\n'
      'Será que você consegue adivinhar qual foi?')

acertou = False
palpites = 0

while not acertou:
      chute = int(input('Qual seu palpite? '))
      palpites += 1
      if valor_secreto == chute:
            acertou = True
      else:
            if chute < valor_secreto:
                  print('Mais... Tente mais uma vez.')
            elif chute > valor_secreto:
                  print('Menos... Tente mais uma vez.')

print('Acertou com {} tentativas. Parabéns!'.format(palpites))