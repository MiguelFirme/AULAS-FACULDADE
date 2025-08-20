funcionarios = {}
while True:
    nome: input("Digite o nome: ")
    salario: float(input("Digite o salário:"))
    
    funcionarios[nome] = salario

    opcao = input("Deseja continuar a operação? [S/N]: ")
    if opcao == "N":
        break

print("Lista de funcionários: ",funcionarios)

remover= input("Qual funcionário vc deseja excluir?: ")

funcionarios .pop(remover)

print("Lista de funcionários atualizada:",funcionarios)
