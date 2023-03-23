# Exercício calcular IMC

'''
Faça um programa que receba a altura e o peso do usuário e calcule o seu IMC utilizando a fórmula abaixo:
imc = peso / (altura*altura)
'''

# Resolução
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / (altura**2)

print(f"Seu IMC é: {imc:.2f}")