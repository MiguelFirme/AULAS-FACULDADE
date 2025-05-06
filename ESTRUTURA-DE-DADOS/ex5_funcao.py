def imprimir_dados(num):
    if num >= 0:
        print ("Numero: ",num," é positivo")
    else:
        print ("numero: ",num," é negativo")
    return 

while  True:
       numero = int(input("Digite um numero inteiro:  "))
     
       #chamada da funcao 
       imprimir_dados(numero)
   
       opcao = input("Deseja continuar S ou N ? ").upper()
       if opcao == "N":
            break
