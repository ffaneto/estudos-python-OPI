ent = int(input())

h = ent // 3600

restoSeg = ent % 3600

min = restoSeg // 60

seg = restoSeg % 60

print(f'{h}:{min}:{seg}')


# 3800 segundos são iguais a 1 hora e 200 segundos, são 1 hora 3 minutos e 20 segundos