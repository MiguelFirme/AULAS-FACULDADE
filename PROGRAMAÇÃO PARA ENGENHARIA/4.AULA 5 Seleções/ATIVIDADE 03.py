print("F-Feminino, M-Masculino")
sexo = input("Indique seu sexo: ").upper()

match sexo:
     case "F":
           print("Sexo: Feminino")
     case "M":
           print("Sexo: Masculino")
     case _:
           print("Sexo Não informado")
           

      
