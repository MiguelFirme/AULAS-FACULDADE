nome = input ("Digite seu nome: ")
idade = float(input("Digite uma idade: "))

#Verificação
if idade <3:
    print(nome,"é um Bebê!")
elif idade >=4 and idade <=11:
    print(nome,"é uma criança!")
elif idade >=12 and idade <=17:
    print(nome,"é um adolecente!")
elif idade >=18 and idade<=60:
    print(nome,"é um adulto!")
elif idade>=61:
    print(nome,"é um senhor!")
    
