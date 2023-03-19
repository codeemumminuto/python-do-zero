# Exercício

'''
Faça um programa que receba a altura e o peso do usuário
e calcule o seu IMC utilizando a fórmula abaixo
'''

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

IMC = peso / (altura**2)

print(f"Seu imc: {IMC:.3f}")