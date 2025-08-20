raio = float(input("Digite o valor do raio: "))

if raio < 0:
    print("Vaores negativos não são permitidos")

else:
    area = 3.14159 * ( raio**2 )
print("A área do círculo de raio",raio," é {:.2f}".format(area))
