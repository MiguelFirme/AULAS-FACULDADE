vv = int(input("Indique a velociade da via em km/h: "))
vm = int(input("indique a velocidade do motorista em km/h: "))
ve = vm - vv

if ve > 0 and ve <= 10:
    print("O valor da multa será de R$85,13 e sujeito a 3 pontos na carteira")

elif ve >= 11 and ve <= 30:
    print("O valor da multa será de R$127,69 e sujeito a 5 pontos na carteira")

elif ve >= 31:
    print("O valor da multa será de R$574,69 e sujeito a 7 pontos na carteira")

else:
    print("Vel. Normal")
    
