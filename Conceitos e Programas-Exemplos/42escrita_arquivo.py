# Escrevendo em um arquivo

arquivo = open("pessoas.txt", "a")

lista = ["Frutas\n", "Verduras\n", "Legumes\n"]
arquivo.writelines(lista)

arquivo.close()
