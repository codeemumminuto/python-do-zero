# Exercício média

'''
Faça um programa que receba duas notas de um aluno e diga
se ele foi aprovado ou não

nota 7 ou superior: Aprovado
menor que 7: reprovado
'''

# Resolução
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1 + nota2)/2

if(media >= 7):
    print(f"Aprovado com média {media:.2f}")
else:
    print(f"Reprovado com média {media:.2f}")