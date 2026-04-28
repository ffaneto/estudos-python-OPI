a = int(input())

b = int(input())

ini = min(a,b)
fim = max(a,b)

for i in range(ini, fim + 1):
    print(i, end= " ")