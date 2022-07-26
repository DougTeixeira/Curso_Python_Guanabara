jogadores = []
jogador = {}
gols = []
total = 0
while True:
    jogador['nome'] = str(input('Nome: ')).strip().title()
    perg1 = int(input(f'Quantas partidas {jogador["nome"]} fez? '))
    for i in range(1, perg1 + 1):
        gols.append(int(input(f'Quantos gols na partida {i}? ')))
    jogador['gols'] = gols[:]
    total += sum(gols)
    jogador['total'] = total
    jogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()
    perg2 = ' '
    while perg2 not in 'SN':
        perg2 = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if perg2 == 'N':
        break
print('-='*40)
print('Cod', end=' ')
for k, v in enumerate(jogadores):
    for i in v.keys():
        print(f'{str(i):<15}', end='')
        break
print()
for k, v in enumerate(jogadores):
    print(f'{k:>3}', end=' ')
    for i in v.values():
        print(f'{str(i):<15}', end='')
    print()
print('-='*40)
while True:
    busca = int(input('Mostrar dados de qual jogaodor? [999 para parar]: '))
    if busca == 999:
        break
    elif busca >= len(jogadores):
        print(f'Erro. Não existe jogador com código {busca}.')
    else:
        print(f' --- LEVANTAMENTO DO JOGADOR: {jogadores[busca]["nome"]}')
        for k, v in enumerate(jogadores[busca]['gols']):
            print(f' --- No {k+1}° jogo, fez {v} gols.')
        print('-=' * 40)
print(f'{"<<< VOLTE SEMPRE >>>":>30}')