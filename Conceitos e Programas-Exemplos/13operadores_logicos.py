# Operadores lógicos

# and - Todas as expressões verdadeiras
# or - Pelo menos 1 expressão verdadeira
# not - Inverte a expressão

# Exemplo 1
sou = input("Digite: ")
idade = int(input("Idade: "))

if(sou == "homem" and idade >= 18):
    print("Deve tirar a reservista")
elif(sou == "homem" and idade < 18):
    print("Ainda não precisa tirar reservista, só com 18 anos!")
else:
    print("Não precisa tirar reservista!")

# Exemplo 2
estado = input("Digite o seu estado: ")

if(estado == "pernambuco" or estado == "bahia"):
    print("A transportadora atende ao seu estado!")
else:
    print("Infelizmente a transportadora ainda não atende ao seu estado")

# Exemplo 3
doente = True

if(not doente): # Irá inverter o valor boleano da variável doente
    print("Pode entrar na loja")
else:
    print("Não pode entrar na loja")