input("digite o nome do aluno: ")
n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))
n3 = float(input("digite a terceira nota: "))

media=(n1+n2+n3)/3
print("Média:",media)

#verificação
if media < 5:
    print("Situação do aluno: REPROVADO")
elif((media > 5) and (media < 7)):
    print("Situação do aluno: EM RECUPERAÇÃO")
elif media >= 7:
    print("Situação do aluno: APROVADO")
