print('Gerador de PA')
print('='*40)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

termo = primeiro
count = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while count <= total:
        print('{} ->'.format(termo), end=' ')
        termo += razao
        count += 1
    print('PAUSA')
    mais = int(input('Quantos termos vc quer mostrar a mais? '))
print('Progessão finalizada com {} termos mostrados.'.format(total))