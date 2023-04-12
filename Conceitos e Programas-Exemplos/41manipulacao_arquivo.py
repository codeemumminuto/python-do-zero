# Manipulação de arquivos
# Exemplos: .txt e .csv

# w (write): Abre um arquivo no modo escrita mas
# substitui o conteúdo que já existe no arquivo

# a (append): Também modo escrita, mas mantém

# r (read): Abre o arquivo no modo leitura

arquivo = open("pessoas.txt", "a")
arquivo.close()
