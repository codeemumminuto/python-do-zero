# Operador in
# String, Lista(ainda não vimos), sequencia range

# Com string
frase = "ola mundo"

if("a" in frase):
    print("Letra está na frase")
else:
    print("A letra não está na frase")


# Com sequência retornada pela função range
sequencia = range(1,10)

if(20 in sequencia):
    print("Está na sequência")
else:
    print("Não está na sequência")