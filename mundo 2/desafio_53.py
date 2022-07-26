frase = str(input('Digite uma frase palindromo: ')).strip().upper()
palavras = frase.split(' ')
juntas = ''.join(palavras)
inverso = ''
for letra in range(len(juntas) - 1, -1, -1):
    inverso += juntas[letra]
print('O inverso de {} é {}.'.format(juntas, inverso))
if juntas == inverso:
    print('É um palindromo')
else:
    print('A frase não é um palindromo')
# if ''.join(frase.split(' '))[:] == ''.join(frase.split(' '))[::-1]:
#     print('a frase {}, é um palindromo'.format(frase))
# else:
#     print('É um simples frase, ',frase)