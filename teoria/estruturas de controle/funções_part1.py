# def soma(a, b):
#     print(a + b)
# soma(5, 4)  # resulta em 9
# ou soma(a=5, b=4)


# def soma(a, b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'A soma A + B = {s}')
# soma(5, 6)
# resulta em
# A = 5 e B = 6
# A soma A + B = 11


# def contador(*num):
#     tam = len(num)
#     print(f'Recebi os valores {num} e são ao todo {tam} números.')
# contador(5, 4, 3, 2, 1)
# contador(3, 2, 1)
# contador(4, 3, 2, 1)


# def soma(*num):
#     s = 0
#     for i in num:
#         s += i
#     print(f'A soma dos valores {num} é igual a {s}')
# soma(4, 5, 1)
# soma(5, 4, 3, 2, 1)


# valores = [5, 4, 6, 8, 1]
# def dobra(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos += 1
# dobra(valores)
# print(valores)