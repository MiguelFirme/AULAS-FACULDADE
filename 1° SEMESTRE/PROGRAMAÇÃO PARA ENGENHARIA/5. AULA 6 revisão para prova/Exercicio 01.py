print( "Dobro / Area / Desconto")
calculo = input("Digite a operação desejada: ").upper()

match calculo:

    case "DOBRO":
        n = float(input("Digite o valor desejado: "))
        dobro = (n) * 2
        print ("O dobro do valor é:",dobro)

    case "AREA":
        l = float(input("Digite a largura: "))
        c = float(input("Digite o comprimento; "))
        a = l * c
        print ("A área total é de:",a)

    case "DESCONTO":
        vr = float(input("Indique o valor da compra: "))
        des = int(input("Indique a % do desconto: "))
        des = vr * ( des / 100)
        total = vr - des
        print("O total a pagar com desconto: R$",total)
