# Praticando and e o or

'''
Faça um programa que receba 3 variáveis com as medidas de um triângulo e diga 
se ele é
Equilátero: 3 lados iguais
Isosceles: 2 lados iguais
Escaleno: Nenhum lado igual
'''

# Resolução
lado1 = float(input("Digite o lado 1"))
lado2 = float(input("Digite o lado 2"))
lado3 = float(input("Digite o lado 3"))

if(lado1 == lado2 and lado2 == lado3):
    print("Equilátero")
elif(lado1 == lado2 or lado2 == lado3 or lado3 == lado1):
    print("Isósceles")
else:
    print("Escaleno")