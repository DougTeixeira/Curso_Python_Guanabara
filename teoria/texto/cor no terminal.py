#ANSI: escape sequence

# \033[stylo;texto;fundom
# \033[0;33;44m          estrutura do codigo

# stylo => 0 é nada, 1 negrito, 4 sublinhado e 7 invertido
# texto => vai de 30 a 37, cada um é uma cor
# fundo => vai do 40 a 47, cada um é uma cor e é igual ao texto em sequencia

# cores
# 30/40 branco ou preto, 31/41 vermelho, 32/42 verde, 33/43 amarelo, 34/44 azul, 35/45 roxo
# 36/46 azul marinho, 37/47 cinza.

# TESTE em branco com fundo vermelho
print('\033[1;30;41mTESTE\033[m')
