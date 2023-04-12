# Exercício lista

lista = []
continua = "s"

while(continua == "s"):
    print("Lista atual:")
    for item in lista:
        print(item)

    print("\nO que deseja fazer?")
    print("1. Adicionar uma tarefa à lista;")
    print("2. Remover uma tarefa da lista;")
    escolha = int(input("Escolha: "))

    if(escolha == 1):
        item = input("Digite o nome da tarefa: ")
        lista.append(item)
    elif(escolha == 2):
        item = input("Digite o nome da tarefa que deseja remover: ")
        lista.remove(item)
    else:
        print("Escolha inválida!!")

    continua = input("Deseja continuar?(s/n) ")
    print("\n")

print("lista final: ")
for item in lista:
    print(item)

'''
Faça um programa que declare uma lista vazia
e continue solicitando uma ação ao usuário
enquanto ele quiser continuar.

As ações são: Adicionar uma tarefa à lista e 
Remover uma tarefa da lista.

O programa deve imprimir a lista atualizada
toda vez antes da ação do usuário, algo como isso:
'''