n = int(input())


dias = 0
acessos = 0

for i in range(1, n + 1):
    acesso_hoje = int(input())
    acessos+=acesso_hoje
    dias +=1

    if(acessos >= 1000000):
        break

print(dias)