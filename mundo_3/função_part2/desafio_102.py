def fatorial(n, show=False):
    """
    -> Calcular o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: Retorna o valor do fatorial do número n.
    """
    f = 1
    for i in range(n, 0, -1):
        f *= i
        if show == True:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f


print(fatorial(1))
print(fatorial(5, True))
print(fatorial(4, False))
help(fatorial)