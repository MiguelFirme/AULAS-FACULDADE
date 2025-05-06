def imprimir_dados(num):
    if (num % 2) == 0:
        print ("Numero: ",num," é par")
    else:
        print ("numero: ",num," é ímpar")
    return 

while  True:
       numero = int(input("Digite um numero inteiro:  "))
     
       #chamada da funcao 
       imprimir_dados(numero)
   
       opcao = input("Deseja continuar S ou N ? ").upper()
       if opcao == "N":
            break
