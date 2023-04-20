# With
# Parar de usar o arquivo.close()

with open ("pessoas.txt", "r") as arquivo:
    lista = arquivo.readlines()

for linha in lista:
    print(linha)