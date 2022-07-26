valor = int(input('Digite o valor do produto: '))
print('Escolha o metodo de pagamento, digitando o numero:')

metodo = int(input('a vista no dinheiro: 1\n'
               'a vista no cartão: 2\n'
               'em duas vezes no cartão: 3\n'
               'em três vezes no cartão: 4\n'
               'Digite o metodo: '))

if metodo == 1:
    print('O valor a ser pago é: {}'.format(valor*0.9))
elif metodo == 2:
    print('O valor a ser pago é: {}'.format(valor*0.95))
elif metodo == 3:
    print('O valor a ser pago é: {}, com parcelas de 2x de {}'.format(valor, valor/2))
elif metodo == 4:
    print('O valor a ser pago é: {}, com parcelas de 3x de {}'.format(valor * 1.2, (valor * 1.2)/3))