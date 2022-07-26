print('-'*30)
print('{:^30}'.format('BANCO CEV'))
print('-'*30)

valor = int(input('Qual valor você quer sacar? R$ '))
count50 = count20 = count10 = count1 = 0
while True:
    if valor >= 50:
        count50 += 1
        valor -= 50
    elif valor >= 20:
        count20 += 1
        valor -= 20
    elif valor >= 10:
        valor -= 10
        count10 += 1
    elif valor >= 1:
        valor -= 1
        count1 += 1
    else:
        break
if count50 != 0:
    print(f'Você recebeu {count50} notas de 50')
if count20 != 0:
    print(f'Você recebeu {count20} notas de 20')
if count10 != 0:
    print(f'Você recebeu {count10} notas de 10')
if count1 != 0:
    print(f'Você recebeu {count1} notas de 1')