# tratamento de exceções
# pré-definidas

try:
    num = int(input("Digite um número: "))
    num2 = int(input("Digite outro: "))
    print(num/num2)
except ValueError:
    print("Deve ser int!!!")
except ZeroDivisionError:
    print("Não divida por zero!!")
finally:
    print("Chegamos ao fim :D")