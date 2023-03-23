# Exercício habilitação

'''
Faça um programa que receba a idade do usuário e diga se ele já pode
tirar a habilitação ou não
'''

# Resolução
idade = int(input("Digite a sua idade: "))

if(idade >= 18):
    print("Pode tirar a habilitação")
else:
    print("Ainda não pode tirar habilitação")