Nc = int(input("Quantidade de cópias desejadas: "))

Valorlivro = 24.95 * Nc
Desconto = Valorlivro*(35/100)

Ncc = Nc - 1

Vf = ((Ncc * 0.75) + 3) + Desconto

print("valor a pagar: ",round(Vf,2))
