def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! por favor, tente um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usúario.')
            return 0
        else:
            return valor


def leiafloat(msg):
    while True:
        try:
            valor = float(input(msg.replace(',','.')))
        except (ValueError, TypeError):
            print('\033[31mERRO! por favor, tente um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usúario.')
            break
        else:
            return valor


n1 = leiaint('Digite um inteiro: ')
n2 = leiafloat('Digite um numero real: ')


print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')