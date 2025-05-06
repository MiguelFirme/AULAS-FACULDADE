def somar_numeros(valor):
    soma = 0
    for i in range(0,valor+1):
       #acumulador
       soma = soma + i
    print ("Soma dos números menores/iguais a ",valor," = ",soma)
    return 

#principal
numero = int(input("Digite um valor inteiro:  "))  
#chamada da funcao 
somar_numeros(numero)
