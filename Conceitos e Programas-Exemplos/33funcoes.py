# Funções pt 1
# Bloco de código que pode ser reutilizado no programa

def dizer_ola(nome):
    print(60*"*")
    print(f"Olá, bem vindo {nome}")
    print(60*"*")

nome = input("Digite seu nome: ")
dizer_ola(nome)