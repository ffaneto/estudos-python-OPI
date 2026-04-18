lista = [1,2,3,4]

for i in range(len(lista)):
    print(lista[i] + 2)

print()

for i, item in enumerate(lista):
    print(i)

f = 10

print()

while f<=100:
    print(f'{f}')
    f += 10

a =0

print()

for i in range(8) :
    if i ==4:
        print("Encontrei a 4")
        break
    print(f'{i}')
    a+= 1
print(f'{a}')

print()


dias = ['dom', 'seg', 'ter', 'qua', 'chu', 'sex', 'sab']

for dia in dias:
    if (dia == 'chu') :
        print("chu num da")
        continue
    print(f'{dia}')


