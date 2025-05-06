vingadores = ()
herois = ()
demitidos = ()

for contador in range (0,6):
    v = input("Digite o nome do vingador: ")
    vingadores = vingadores + tuple([v])

n = int(input("Deseja adicionar algum herói? se sim, quantos: "))
for contador in range (n):
    a = input("Digite o nome do vingador adicionado: ")
    herois = herois + tuple([a])

vingadores2 = vingadores + herois

nd = int(input("Deseja retirar algum herói? se sim, quantos: "))
for contador in range (nd):
    a = input("Digite o nome do retirados: ")
    demitidos = demitidos + tuple([a])

    if nd in vingadores2:
        vingadores = vingadores - demitidos


print(vingadores)
print(["thor"])