n1 = int(input("Digite o valor inicial: "))
n2 = int(input("Digite o valor final: "))
soma = 0 

for contador in range (n1+1, n2):
    print("Os numeros neste intevalor são:",contador)
    soma = soma + contador

print("A soma dos intervalos é:",soma)