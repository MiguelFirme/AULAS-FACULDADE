def imprimir_dados(funcionario,valor):
    print ("Nome Funcionário: ",funcionario," Salário R$: ",valor)
    return 

while  True:
       nome    = input("Digite nome funcionario:  ")
       salario = float(input("Digite salario R$:  "))
       while (salario <= 0):
              salario = float(input("informe um salário válido!!! =  "))
       
       #chamada da funcao funcionario
       imprimir_dados(nome,salario)
   
       opcao = input("Deseja continuar S ou N ? ").upper()
       if opcao == "N":
            break
