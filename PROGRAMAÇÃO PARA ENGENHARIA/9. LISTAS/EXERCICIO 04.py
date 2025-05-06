caracteres = []
totalvogal = 0
totalconso = 0
for contador in range (0, 10):
    letra = input("Digite aqui seu caracter: ").upper()
    caracteres.append(letra)

    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        totalvogal += 1

    else:
        totalconso += 1

print("Lista de caracteres inseridos:",caracteres)
print("Total de vogais:",totalvogal)
print("Total de consoantes",totalconso)




