a1 = int(input('Digite o primeiro termo: '))
razao = int(input('Razao: '))
print('='*40)
print(' '*10, 'TERMOS DE UMA P.A')
print('='*40)
pa = a1 + (10 - 1)*razao
for i in range(a1,pa + razao, razao):
    print(i, end=' ➡ ')
print('ACABOU')