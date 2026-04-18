list = ["a", "b", "c"]

listb = ["a", 3, "b", True]

print(list[-3], listb[-2])

list [0] = "ab"
print(list[-3])
print(list)
print(listb)

print()

listc = ['a', 'b', 'c', 'd']

for i in listc:
    print(f'{i}')

print()

print(listc)

print()

print(len(listc))
print()

for i in range(len(listc)):
    print(f'{i}, {listc[i]}')