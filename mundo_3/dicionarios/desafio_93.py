jogador = {}
gols = []
jogador['Nome'] = str(input('Nome do jogador: ')).strip().title()
quant = int(input(f'Quantas partidas {jogador["Nome"]}, jogou? '))

for i in range(1, quant+1):
    gols.append(int(input(f'   Quantos gols, {jogador["Nome"]} fez na {i}° partida? ')))
jogador['Gols'] = gols
jogador['Total'] = sum(gols)
print('-='*40)
print(jogador)
print('-='*40)

for k, v in jogador.items():
    print(f'{k}: {v}')
print('-='*40)

print(f'O jogador {jogador["Nome"]}, jogou {quant} partidas.')
for k, v in enumerate(gols):
    print(f'   => Na partida {k+1}, fez {v} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')