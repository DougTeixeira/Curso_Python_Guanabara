def leiaint(frase):
    valor = input(frase)
    while True:
        if valor.strip().isnumeric():
            return valor.strip()
            break
        elif valor.strip() == '':
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            valor = input(frase)
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            valor = input(frase)


n = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o número {n}')