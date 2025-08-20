print("indique a baixo o periodo(M - Matutino / V - Vespertino N - Noturno)")
periodo = input("Digite aqui: ").upper()

match periodo:
    case "M":
        print("Bom dia!")

    case "V":
        print("Boa tarde!")

    case "N":
        print("Boa noite!")

    case (_):
        print("Valor invalido!")
