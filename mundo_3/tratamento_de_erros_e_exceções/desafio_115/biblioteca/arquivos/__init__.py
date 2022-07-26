from mundo_3.tratamento_de_erros_e_exceções.desafio_115.biblioteca.interface import cabeçalho

def arquivoExiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        print(f'Arquivo {arq} não existe.')
        return False
    else:
        print(f'O arquivo {arq} existe.')
        return True


def criarArquivo(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('Erro ao criar arquivo.')
    else:
        print('Arquivo criado com sucesso.')


def lerArquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Erro ao tentar ler arquivo.')
    else:
        cabeçalho('Pessoas Cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>3}')
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na escrita do arquivo.')
        else:
            print(f'Novo registro de {nome} adicionado.')
