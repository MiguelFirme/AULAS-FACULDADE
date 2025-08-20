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
    
    #Verificar se o valor foi digitado na primeira tupla
    if n in A:
        C = C + tuple([n])

print("A união das Tuplas registradas é:",C)