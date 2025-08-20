def calcular_media(n1,n2,n3):
    media = (n1 + n2 + n3)/3
    return media

def verificar_situacao(resul):
    if resul > 6:
        print("Aluno aprovado!")
    if resul >= 4 and resul <= 6:
        print("Aluno em recuperação!")
    if resul < 4:
        print("Aluno reprovado!")
    return
 
while True: 
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    #chamada da função média
    resultado = calcular_media(nota1, nota2, nota3)

    print("Aluno:",nome,"media final:",resultado)

    #chamado da função verificação
    verificar_situacao(resultado)

    opcao = input("Deseja continuar? S/N: ").upper()
    if opcao == "N":
        break