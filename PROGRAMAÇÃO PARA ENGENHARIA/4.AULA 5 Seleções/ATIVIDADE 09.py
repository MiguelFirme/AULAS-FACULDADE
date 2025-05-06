print("CALCULADORA")
n1= float(input(" "))
operacao = input(" ")
n2= float(input(" "))

#CALCULO
if operacao == "+":
    resultado = n1 + n2
    print(resultado)

if operacao == "-":
    resultado = n1 - n2
    print(resultado)

if operacao == "*":
    resultado = n1 * n2
    print(resultado)

if operacao == "/":
    resultado = n1 / n2
    print(resultado)
