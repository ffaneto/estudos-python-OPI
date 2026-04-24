n = int(input())

lista = list(map(int, input().split()))

soma = 0

for numero in lista:
    soma+= numero

print(soma)