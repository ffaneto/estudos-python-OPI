n = int(input())

lista = list(map(int, input().split()))

cont = 0
contAtual = 1

for i in range(len(lista) - 1):
    if lista[i] == lista[i + 1]:
        contAtual += 1

    else:
        contAtual = 1

    if (contAtual > cont):
        cont = contAtual

print(cont)
