frase = str(input('Digite a frase: ')).strip()

print(len(frase))
print('numero de A: ', frase.count('a'))
print('primeiro A aparece na posição: ', frase.find('a')+1)
print('o ultimo A aparece na posição: ', frase.rfind('a')+1)
