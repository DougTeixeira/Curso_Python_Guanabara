try: # operações
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

# except: # caso de falha
#     print('Infelizmente tivemos um problema :')

except ValueError or TypeError:
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir um numero por zero.')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados.')
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
else: # caso dê certo
    print(f'O resultado é {r}.')
finally: # acontece dando certo ou errado
    print('Volte sempre! Muito obrigado!')