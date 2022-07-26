def metade(preço):
    return preço / 2


def dobro(preço):
    return preço * 2


def aumentar(preço, taxa):
    res = preço + (preço*taxa)/100
    return res


def diminuir(preço, taxa):
    res = preço - (preço*taxa)/100
    return res