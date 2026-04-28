n = int(input())

if n == 0 or n == 1:
    n = 1
else:
    for i in range(2, n):
        n *= i

print(n)

