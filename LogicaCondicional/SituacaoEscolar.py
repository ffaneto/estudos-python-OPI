n1 , n2 , n3 = map(int, input().split())
media = n1 + n2 + n3 / 3

if(media <5 ):
    print("Reprovado")
elif(media >= 7):
    print("Aprovado")
else:
    print("Recuperacao")
