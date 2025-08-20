FV = float(input("digite o valor final desejado: "))
n = int(input("digite o tempo de investimento (mensal): "))
i = float(input("digite a rentabilidade do seu investimento(%): "))
I = i / 100
PV = (FV /((1+I)**n))
print("seu valor inicial deve ser de: ",PV)
