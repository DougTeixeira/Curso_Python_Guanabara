print("*-*-" * 20)
print('Analisador de triângulos'.upper())
print("*-*-" * 20)

seg_1 = float(input('Digite o primeiro segmento: '))
seg_2 = float(input('Digite o segundo segmento: '))
seg_3 = float(input('Digite o terceiro segmento: '))

if seg_1 < seg_2 + seg_3 and seg_2 < seg_1 + seg_3 and seg_3 < seg_1 + seg_2:
    print('Os segmentos podem formar um triangulo!')
    if seg_1 == seg_2 == seg_3:
        print('É um triângulo, equilátero.')
    elif seg_1 != seg_2 != seg_3 != seg_1:
        print('É um triângulo, escaleno.')
    else:
        print('É um triângulo, isóceles.')
else:
    print('Os três segmentos não formam um triângulo')