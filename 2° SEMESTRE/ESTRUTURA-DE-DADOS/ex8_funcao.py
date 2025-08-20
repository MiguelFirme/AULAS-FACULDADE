def imprimir_dados(A,B,lim):
    if (A + B) > lim:
       return True
    else:
       return False

while  True:
    valorA = int(input("Digite um valor A:  "))
    valorB = int(input("Digite um valor B:  "))
    limite = int(input("Digite um valor para limite:  "))
    #chamada da funcao 
    resultado = imprimir_dados(valorA, valorB, limite)
    print("Soma valor A e valor B é maior limite? ",resultado)
   
   opcao = input("Deseja continuar S ou N ? ").upper()
   if opcao == "N":
      break
