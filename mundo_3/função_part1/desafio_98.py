from time import sleep

def contagem(a, b, c):
    print(f'Contagem de {a} até {b} de {c} em {c}.')
    if c < 0 and a > b:
        for i in range(a, b-1, c):
            print(i, end=' ', flush=True)
            sleep(0.5)
        print('FIM!')
        sleep(0.5)
    if c < 0 and a < b:
        for i in range(a, b-1, (-c)):
            print(i, end=' ', flush=True)
            sleep(0.5)
        print('FIM!')
        sleep(0.5)
    elif b > a:
        for i in range(a, b+1, c):
            print(i, end=' ', flush=True)
            sleep(0.5)
        print('FIM!')
        sleep(0.5)
    elif a >b :
        for i in range(a, b+1, (-c)):
            print(i, end=' ', flush=True)
            sleep(0.5)
        print('FIM!')
        sleep(0.5)

print('-='*30)
sleep(0.5)
print('Contagem de 1 até 10 de 1 em 1:')
sleep(0.5)
for i in range(1, 11, 1):
    print(i, end=' ', flush=True)
    sleep(0.5)
print('FIM!')
sleep(0.5)
print('-='*30)
sleep(0.5)
print('Contagem de 10 até 0 de 2 em 2:')
sleep(0.5)
for i in range(10, -1, -2):
    print(i, end=' ', flush=True)
    sleep(0.5)
print('FIM!')
sleep(0.5)
print('-='*30)
print('Agora é sua vez de personalizar a contagem!')
sleep(0.5)
a = int(input('Inicio: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contagem(a, b, c)