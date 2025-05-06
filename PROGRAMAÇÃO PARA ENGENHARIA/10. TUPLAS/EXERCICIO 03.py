N = int(input("Quantos numeros deseja cadastrar?: "))
A = ()
B = ()
C = ()

for contador in range (N):
    n = int(input("Digite o valor: "))
    A = A + tuple([n])

N2 = int(input("Quantos numeros deseja cadastrar na segunda tupla?: "))

for contador in range (N):
    n = int(input("Digite o valor: "))
    B = B + tuple([n])


C = (A + B)

print("A união das tuplas resultaram em:",C)
