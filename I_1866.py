c = int(input())
n = []

for i in range(0, c):
    n.append(int(input()))

resultados = []

for numero in n:
    termos = []
    for vezes in range(numero):
        if len(termos) == 0:
            termos.append(1)
        elif termos[len(termos)-1] == 1:
            termos.append(-1)
        else:
            termos.append(1)
    resultados.append(sum(termos))

for resultado in resultados:
    print(resultado)
