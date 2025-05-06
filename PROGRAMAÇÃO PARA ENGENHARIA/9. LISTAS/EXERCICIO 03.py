notas = []

for contador in range (0,4):
    nota = float(input("Digite a nota: "))
    notas.append(nota)

media = sum (notas)/4

print("Notas do aluno:",notas)
print("Média geral do aluno",media)