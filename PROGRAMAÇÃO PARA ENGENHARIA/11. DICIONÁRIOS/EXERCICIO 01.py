agenda = {}

n = int(input("Quantos nomes deseja cadastrar? "))

for i in range (n):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo; M ou F: ")
    contato = [] 
    contato.append(idade)
    contato.apend(sexo)
    agenda.update({nome: contato})

print (agenda)

