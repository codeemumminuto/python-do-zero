# Laço while pt 3

continua = "s"
soma = 0

while(continua == "s"):
    num = int(input("digite um número: "))
    soma += num

    continua = input("Deseja continuar?(s/n): ")

print(f"Fim do programa, soma total: {soma}")