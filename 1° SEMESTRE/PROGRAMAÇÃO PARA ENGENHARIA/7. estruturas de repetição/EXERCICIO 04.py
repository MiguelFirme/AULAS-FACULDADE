N = int(input("Digite um numero: "))
fatorial = 1

for contador in range(1, N+1):
   fatorial = fatorial * contador
   contador= +1

print(f"Fatorial de {N}:",fatorial)