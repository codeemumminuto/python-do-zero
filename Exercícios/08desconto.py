# Exercício calcular desconto

'''
Faça um programa que calcule o desconto de um produto de acordo com a forma
de pagamento escolhida pelo usuári

À vista: 10% desconto
À vista no cartão: 5% desconto
Parcelado no cartão: preço normal
'''

# Resolução
preco = float(input("Digite o preço do produto"))

print("Formas de pagamento:\n1. À vista\n2. À vista no cartão\n3. Parcelado no cartão")
escolha = int(input("Escolha: "))

if(escolha == 1):
    resultado = preco * 0.90
    print(f"Preço final: {resultado}")
elif(escolha == 2):
    resultado = preco * 0.95
    print(f"Preço final: {resultado}")
elif(escolha == 3):
    print(f"Preço final: {preco}")
else:
    print("Opção inválida")