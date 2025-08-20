print ("Estado civil: C-casado / S-solteiro / V-Viúvo")
estado = input ( "Digite uma das opções acima: ").upper()

match estado:
    case "C":
            print("estado civil: CASADO")
    case "S":
            print("estaudo civil: SOLTEIRO")
    case "V":
            print("estado civil: VIÚVO")
