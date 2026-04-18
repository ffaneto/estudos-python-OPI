
aprovados = 0
maiorAltura = 0

n = int(input())

alturas = list(map(float,input().split()))

for altura in alturas:
    if altura >= 1.90:
        aprovados +=1
    if altura > maiorAltura:
        maiorAltura = altura

print(f'Aprovados: {aprovados}')
print(f'Maior altura: {maiorAltura:.2f}')