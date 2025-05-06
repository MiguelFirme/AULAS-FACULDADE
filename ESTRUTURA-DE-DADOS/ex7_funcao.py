def adicao(v1,v2):
    res = v1 + v2
    print ("Resultado: ",valor1," + ",valor2," = ",res)
    return 

def subtracao(v1,v2):
    res = v1 - v2
    print ("Resultado: ",valor1," - ",valor2," = ",res)
    return 

def multiplicacao(v1,v2):
    res = v1 * v2
    print ("Resultado: ",valor1," * ",valor2," = ",res)
    return 

def divisao(v1,v2):
    res = v1 / v2
    print ("Resultado: ",valor1," / ",valor2," = ",res)
    return 

while True:
    print ("Operações da Calculadora: ")
    print ("1 - Adição        ")
    print ("2 - Subtração     ")
    print ("3 - Multiplicação ")
    print ("4 - Divisão       ")
    print ("5 - Sair Programa ")
    opcao = int(input("Escolha a opção desejada; "))
    if (opcao == 5):
        print ("Fim do programa.....")
        break
    
    valor1 = int(input("Digite primeiro valor: "))
    valor2 = int(input("Digite segundo  valor: "))

    if (opcao == 1):
        adicao(valor1,valor2)
    if (opcao == 2):
        subtracao(valor1,valor2)
    if (opcao == 3):
        multiplicacao(valor1,valor2)
    if (opcao == 4):
        divisao(valor1,valor2)
