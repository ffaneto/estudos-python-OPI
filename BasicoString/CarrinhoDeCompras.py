lista = []

while True:
    n = input()

    if(n == "fim"):
        break

    lista.append(n)

lista.sort()
for produto in lista:
    print(produto)