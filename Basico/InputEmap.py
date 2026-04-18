a = input("Digite os nomes separados por espaço")

b = a.split()

print(f"{b}")

c = input("Denovo")

d = list(map(float, c.split()))

print(f"{d}")

print(" ".join(b))

print(f'inicio {a}')

x = ['a', 'b']

x.append("g")

print(x)

for i in range(len(x)) :
    print(f'{i}, {x[i]}')

y = ["a", "b", "c", "d"]

print(f'{y}')

y.insert(4, "e")

print(f'{y}')

del y[4]
print(f'{y}')

y.remove("d")

print(f"{y}")

a = y.pop(0)

print(y)

b = y.pop()

print(f"{y}")

y = ["a", "b", "c", "d"]

print(len(y))

z = [2, 1, 3, 4, 5]

print("Original: ")

print(z)

z.sort()

print("Sort: ")

print(z)

print("Sorted: ")

z = [2, 1, 3, 4, 5]

zSorted = sorted(z)

print(zSorted)

