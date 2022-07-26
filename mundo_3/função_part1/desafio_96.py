def area(l, c):
    a = l*c
    print(f'A área de um terreno {l:.1f} x {c:.1f} é de {a:.1f} m^2')


print('  CONTROLE DE TERRENOS')
print('-'*40)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
