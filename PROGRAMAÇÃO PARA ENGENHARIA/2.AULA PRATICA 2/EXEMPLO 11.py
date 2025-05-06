nome = input("Digite um nome:")
ht = float(input("Digite as horas trabalhadas:"))
vh = float(input("Digite o valor da hora:"))

salariobruto = ht * vh
salariodesc = salariobruto - (salariobruto * 0.02)


print(nome,"seu salário final será de:",salariodesc)
