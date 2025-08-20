sal = float(input("Digite o valor do salário: "))

if sal <= 1000:
    novo = sal + (sal * 0.10)
    print("O novo salário é de",novo)

else:
    novo = sal + (sal *0.05)
    print("O novo salário é de",novo)
    
