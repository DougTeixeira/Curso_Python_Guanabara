cidade = str(input('Nome da cidade: ')).strip()

if cidade.split(' ')[0].capitalize() == 'Santo':
    print('A primeira palavra no nome da cidade começa com Santo')

else:
    print('A primeira palavra do nome da cidade não começa com Santo')
