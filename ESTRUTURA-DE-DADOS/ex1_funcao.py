def calcular_media(n1,n2):
    media = (n1 + n2)/2
    return media

while  True:
   nome = input("Digite nome do aluno:  ")
   nota1 = float(input('entre com a primeira nota:  '))
   nota2 = float(input('entre com a segunda  nota:  '))
   #chamada da funcao
   resultado = calcular_media(nota1,nota2)
   
   print ("Média final : ",resultado)
   
   opcao = input("Deseja continuar S ou N ? ").upper()
   if opcao == "N":
        break
