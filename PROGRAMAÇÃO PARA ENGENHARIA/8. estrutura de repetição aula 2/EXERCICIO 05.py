n = int(input("Digite um valor: "))
maior = n
menor = n

for contador in range (0,10):
    n = int(input("Digite o proximo valor: "))
     
    if n > maior:
       maior = n

    elif n < menor:
        n = menor

print("Maior valor digitado foi:",maior)
print("Menor valor digitado foi:",menor)