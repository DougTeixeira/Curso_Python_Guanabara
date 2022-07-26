def leiaint(msg):
    while True:
        try:
            n = int(input(msg).strip())
        except (ValueError, TypeError):
            print('\33[31mERRO: Por favor, digite um valor valido\33[m.')
        except UnboundLocalError:
            print('\33[31mVocê não digitou nada.\33[m')
        except KeyboardInterrupt:
            print('\33[31mEntrada de dados interrompida pelo usúario.\33[m')
            return 0
        else:
            return n


def linha(tam=42):
    print('\33[36m-\33[m'*tam)


def cabeçalho(msg):
    linha()
    print(f'\33[35m{msg}\33[m'.center(42))
    linha()

def menu(*lista):
    c = 1
    for item in lista:
        print(f'\33[32m{c}\33[m - \33[33m{item}\33[m')
        c += 1
    linha()
    opc = leiaint('\33[34mSua opção: \33[m')
    return opc