from time import sleep


def maiorvalor(*nums):
    maior = count = 0
    print('-=' * 30)
    sleep(0.5)
    print('Analisando os valores passados...')
    sleep(0.5)
    for i in nums:
        print(i, end=' ', flush=True)
        sleep(0.5)
        if count == 0 or maior < i:
            maior = i
            count += 1
    sleep(0.5)
    print(f'Foram informados {len(nums)} valores ao todo.')
    sleep(0.5)
    print(f'O maior valor informado foi {maior}')
    sleep(0.5)


maiorvalor(6, 5, 4, 3, 2, 1)
maiorvalor(9, 20, 30, 1)
maiorvalor(70, 60, 50)
maiorvalor()