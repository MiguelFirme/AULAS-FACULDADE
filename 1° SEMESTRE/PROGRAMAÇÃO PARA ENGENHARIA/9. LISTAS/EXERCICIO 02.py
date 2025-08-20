numeros = []

for contador in range(0,10):
    valor = int(input("Digite um valor: "))
    numeros.append(valor)

print("Lista de numeros inseridos:",numeros)
numeros.reverse()
print("Lista ao contrario de numeros inseridos:",numeros)