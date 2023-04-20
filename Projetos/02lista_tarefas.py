# Projeto lista de tarefas!
from datetime import datetime

def validar_data(data_hora):
    try:
        datetime.strptime(data_hora, "%d/%m/%Y %H:%M")
        return True
    except:
        return False

def adicionar_tarefa(nome, descricao, data, hora, lista):
    lista.append(nome + ";" + descricao + ";" + data + ";" + hora)

def listar_tarefas(lista):
    for i, tarefa in enumerate(lista):
        #nome;descricao;data;hora
        print(f"Tarefa número {i+1}")
        print("-"*30)
        informacoes = tarefa.split(";")
        print(f"Nome: {informacoes[0]}")
        print(f"Descrição: {informacoes[1]}")
        print(f"Data: {informacoes[2]}")
        print(f"Hora: {informacoes[3]}")
        print("\n")

def remover_tarefa(indice, lista):
    lista.pop(indice-1)

lista = []

print("Olá, bem-vindo ao meu projeto!")
while True:
    print("\nMenu:")
    print("1. Adicionar uma tarefa")
    print("2. Listar tarefas")
    print("3. Remover uma tarefa")
    print("4. Editar uma tarefa")
    print("5. Sair")

    try:
        escolha = int(input("Escolha: "))
    except ValueError:
        print("Opção inválida, escolha um inteiro!")
        continue

    if(escolha == 1):
        nome_tarefa = input("Digite o nome da tarefa: ")
        descricao_tarefa = input("Digite a descrição da tarefa: ")
        data_tarefa = input("Digite a data em formato dia/mes/ano: ")
        hora_tarefa = input("Digite uma hora em formato hora:minuto: ")

        data_hora = data_tarefa + " " + hora_tarefa

        if(validar_data(data_hora)):
            adicionar_tarefa(nome_tarefa, descricao_tarefa, data_tarefa, hora_tarefa, lista)
        else:
            print("Erro, data ou hora inválidas!")

    elif(escolha == 2):
        listar_tarefas(lista)
    
    elif(escolha == 3):
        listar_tarefas(lista)
        try:
            num_tarefa = int(input("Digite o número da tarefa: "))
            remover_tarefa(num_tarefa, lista)
        except ValueError:
            print("Escolha um inteiro!")