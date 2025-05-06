def imprimir_dados(funcionario,valor):
    if valor is null:
        valor = 9000
    print ("Nome Funcionário: ",funcionario," Salário R$: ",valor)
    return 

while  True:
       nome    = input("Digite nome funcionario:  ")
       salario = float(input("Digite salario R$:  "))
       
       #chamada da funcao funcionario
       imprimir_dados(nome,salario)
   
       opcao = input("Deseja continuar S ou N ? ").upper()
       if opcao == "N":
            break
