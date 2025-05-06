nome = (input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))

if idade <= 15:
    print(nome,", Você ainda não possui a idade mínima para doação!")

elif idade >= 16 and idade <=17 and peso > 50:
    print(nome,", Você só poderá doar acompanhado de um responsavel legal!")
  
elif idade >= 18 and idade <=69 and peso > 50:
    print(nome,",Você pode fazer a doação!")

elif idade > 69:
    print (nome,",Sentimos muito, mas você já ultrapassou a idade limite")

else:
    print("Não possui peso mínimo adequado para doação")

