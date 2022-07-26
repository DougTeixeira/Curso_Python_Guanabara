def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita  várias).
    :param sit: valor opcional se deve ou não adicionar ou não situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dic = {}
    dic['Total'] = len(n)
    dic['Maior'] = max(n)
    dic['Menor'] = min(n)
    dic['Média'] = sum(n)/len(n)
    if sit == True:
        if 7 <= dic['Média'] <= 10:
            dic['Situação'] = 'Boa'
        elif 5 <= dic['Média']:
            dic['Situação'] = 'Razoavel'
        elif 0 <= dic['Média']:
            dic['Situação'] = 'Ruim'
        else:
            print('Valor invalido')
    return dic


resp = notas(2, 8, 10, 8, sit=True)
print(resp)
help(notas)