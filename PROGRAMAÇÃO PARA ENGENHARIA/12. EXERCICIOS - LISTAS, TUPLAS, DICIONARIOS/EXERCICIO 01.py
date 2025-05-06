def calcular_media(n1,n2,n3):
    media = (n1 + n2 + n3)/3
    return media

while True: 
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    #chamada da função
    resultado = calcular_media(nota1, nota2, nota3)

    print("A media final é:",resultado)

    opcao = input("Deseja continuar? S/N: ").upper()
    if opcao == "N":
        break
    print("Processo encerrado")