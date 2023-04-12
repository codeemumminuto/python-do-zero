# Praticando um pouco mais funções

def eh_primo(num):
    # Número primo só tem 2 divisores!
    divisores = 0
    for i in range(1,num+1): # fim +1
        if num % i == 0:
            divisores += 1
    
    if divisores == 2:
        return True
    else:
        return False
    

numero = int(input("Digite um número: "))
print(eh_primo(numero))