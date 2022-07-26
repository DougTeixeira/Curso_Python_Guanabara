from random import randint

print('='*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('='*30)

count = 0
while True:
    jogada_pc = randint(1, 10)
    jogada_p = int(input('Digite um valor: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    soma = jogada_p + jogada_pc

    print('Você jogou {} e o computador {}. Total de {}.'.format(jogada_p, jogada_pc, soma))
    print('Deu PAR' if soma % 2 == 0 else 'Deu IMPAR')
    if escolha == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            count += 1
        else:
            print('Você PERDEU!')
            break
    elif escolha == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!')
            count += 1
        else:
            print('Você PERDEU!')
            break
    print('vamos jogar novamente!')
print('VocÊ conseguiu vencer {} vezes.'.format(count))