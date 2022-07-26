prim = int(input('Primeiro valor: '))
seg = int(input('Segundo valor: '))

while True:
    opcao = int(input('   [1] somar\n'
                  '   [2] multiplicar\n'
                  '   [3] maior\n'
                  '   [4] novos números\n'
                  '   [5] sair do programa\n'
                  '>>>>> Qual é a sua opção? '))
    if opcao == 1:
        print('A soma entre {} + {} é {}.'.format(prim, seg, prim + seg))
    elif opcao == 2:
        print('O resultado de {} x {} é {}.'.format(prim, seg, prim * seg))
    elif opcao == 3:
        if prim > seg:
            print('O primeiro valor {} é maior que o segundo {}.'.format(prim, seg))
        elif prim < seg:
            print('O segundo valor {} é maior que o primeiro {}.'.format(seg, prim))
        else:
            print('Os valores sao iguais.')
    elif opcao == 4:
        print('Informe os novos valores:')
        prim = int(input('Primeiro valor: '))
        seg = int(input('Segundo valor: '))
    elif opcao == 5:
        break