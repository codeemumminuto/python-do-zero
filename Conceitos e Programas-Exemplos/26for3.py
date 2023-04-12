# For parte 3
# Substituir vogais por *

frase = "Hello World!"
nova_frase = ""
vogais = "aeiou"

for caractere in frase:
    if(caractere in vogais):
        nova_frase += "*"
    else:
        nova_frase += caractere

print(nova_frase)