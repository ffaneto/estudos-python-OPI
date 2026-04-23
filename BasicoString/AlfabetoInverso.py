entrada = input().split()

entrada.sort()

lista_invertida = entrada[::-1]

for nome in lista_invertida:
    print(nome)