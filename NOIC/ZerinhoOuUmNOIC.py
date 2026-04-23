a , b , c = map(int, input().split())

if (a == b and a == c):
    print("*")

elif(a == b and c !=a):
    print("C")

elif(a == c and b!= a):
    print("B")
else:
    print("A")