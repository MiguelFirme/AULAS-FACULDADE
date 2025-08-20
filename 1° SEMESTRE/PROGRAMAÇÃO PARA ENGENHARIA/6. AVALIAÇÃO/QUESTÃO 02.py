print("Digite sua data de nascimento: ")
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

idade = 2024 - ano

if idade < 18:
    print("Você não possui idade suficiente para retirar a CNH!")

else:
    print("Você possui didade suficiente para retirar a CNH!")
    

