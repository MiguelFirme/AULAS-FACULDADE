numero = int(input("Digite o 1 numero: "))
maior = numero
menor = numero 

for contador in range(1, 5):
  numero = int(input('Digite um numero: '))

  if numero > maior:
    maior = numero

  elif numero > menor:
    menor = numero

print("Maior numero é:",maior)
print("Menor numero é:",menor)
