vn = 0 
vp = 0

for acumulador in range (1,6):
    v = int(input("Digite um valor: "))
    
    if v <= 0:
       vn += 1
    else:
       vp += 1

print("Total de numeros positivos digitados:",vp)
print("Total de numeros negativos digitados:",vn)
