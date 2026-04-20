n = int(input())
soma = 0

for i in range(n + 1):
    if (i % 2 == 0):
        soma+=i

print(soma)

soma = 0

for i in range(0, n+1 , 2):
    soma+=i

print(soma)