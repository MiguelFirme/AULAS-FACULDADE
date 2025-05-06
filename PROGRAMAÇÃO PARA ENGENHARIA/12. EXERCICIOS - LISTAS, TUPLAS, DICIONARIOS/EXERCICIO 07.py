def adicao(v1,v2):
    res = v1 + v2
    print ("resultado:",v1,"+",v2,"=",res)
    return

def sub(v1,v2):
    res = v1 - v2
    print ("resultado:",v1,"-",v2,"=",res)
    return

def div(v1,v2):
    res = v1 / v2
    print ("resultado:",v1,"/",v2,"=",res)
    return

def mult(v1,v2):
    res = v1 * v2
    print ("resultado:",v1,"x",v2,"=",res)
    return

while True:
    print("+ | - | / | x ")
    op = input("Escolha a operação desejada: ")
    
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

    if op == "+":
        adicao(valor1,valor2)

    if op == "-":
        sub(valor1,valor2)
    
    if op == "/":
        div(valor1,valor2)

    if op == "x":
        mult(valor1,valor2)