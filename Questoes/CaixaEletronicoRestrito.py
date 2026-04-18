nota50 = 0;
nota10 = 0;

n = int(input())

if (n % 10 !=0):
    print("Saque inválido")
else:
    nota50 = n // 50
    resto =  n % 50

    nota10 = resto //10

print(f"Notas de 50: {nota50}")
print(f"Notas de 10: {nota10}")
