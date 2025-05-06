senha = 2603

for contador in range (0,5):
   tentativa = int(input("Digite sua senha de 4 digitos: "))

   if tentativa != senha:
      print("Senha incorreta")

   elif tentativa == senha:
       print("Bem-vindo!")
       break
else:
     print("Limites de tentativas atigida")
