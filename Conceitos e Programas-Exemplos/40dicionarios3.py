# Percorrendo um dicionário!

'''
frutas = ["Goiaba", "Maracujá", "Maçã"]
precos = [0.50, 0.75, 0.25]
quantidades = [10, 50, 25]

for i in range(3):
    print(f"{frutas[i]} custa {precos[i]} reais e possui {quantidades[i]}x")
'''

frutas = {
    "goiaba":{"preco":0.50,"quantidade":10},
    "maracujá":{"preco":0.50,"quantidade":10},
    "maçã":{"preco":0.50,"quantidade":10}
    }

for chave, valor in frutas.items():
    print(f"{chave} custa {valor['preco']} possui {valor['quantidade']}")
