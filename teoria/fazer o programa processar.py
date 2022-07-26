from time import sleep
print('Processando...')
sleep(2)

for i in range(10, -1, -1):
    print(i, end=' ', flush=True)
    sleep(0.5) # para funcionar precisa do flush = True
print('FIM!')