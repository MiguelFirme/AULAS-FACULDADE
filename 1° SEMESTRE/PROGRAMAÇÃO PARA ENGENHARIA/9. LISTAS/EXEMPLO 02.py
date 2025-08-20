amigos=[]

while True:
    nome = input("Insira o nome do amigo: ")
    amigos.append(nome)
    opcao= input("Deseja continuar a operação? S ou N ").upper()
    if opcao == "N":
        break
print("Lista de amigos:",amigos)