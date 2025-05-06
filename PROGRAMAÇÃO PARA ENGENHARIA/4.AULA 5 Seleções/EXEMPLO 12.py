V = float(input("Indique a tensão: "))
I = float(input("Indique a corrente: "))
R = float(input("Indique a resistencia: "))

#calculo

Vc = I * R

#cmparação

if Vc == V:
    print("O componenete obedece a Lei de Ohm")
else:
    print("O componente não obedece a Lei de Ohm")
    
