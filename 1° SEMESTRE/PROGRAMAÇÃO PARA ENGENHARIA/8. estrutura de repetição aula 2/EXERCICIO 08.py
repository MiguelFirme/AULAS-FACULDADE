menor = 0
maior = 0

for contador in range(1,11):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    if idade < 18:
        menor +=1

    else:
        maior += 1

print("A quantidade de pessoas menores cadastradas foi:",menor)
print("A quantidade de pessoas maiores cadastradas foi:",maior)