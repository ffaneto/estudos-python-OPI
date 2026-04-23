n1 , n2 = map(float, input().split())

if ((n1 + n2 ) / 2 >=7):
    print("Aprovado")
elif((n1 + n2) /2 >=4):
    print("Recuperacao")
else:
    print("Reprovado")