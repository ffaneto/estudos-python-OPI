n = int(input())

lance_maximo = 0
ganhador = ""


for i in range(n):

    c = input()
    v = int(input())

    if(v > lance_maximo):
        ganhador = c
        lance_maximo = v





print(ganhador)
print(lance_maximo)
