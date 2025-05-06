kmi = float(input("Indique Quilometragem inicial: "))
kmf = float(input("Indique Quilometragem Final: "))
dia = int(input("Indique a quantidade de dias de uso: "))

km = kmf - kmi

Vd = dia * 160
Vkm = km * 0.80
Vtotal = Vd + Vkm
print("Valor da diária:",Vd)
print("Valor por Km rodado:",Vkm)
print("valor total a ser pago:",Vtotal)

