ent = int(input())

h = ent // 3600

restoSeg = ent % 3600

min = restoSeg // 60

seg = restoSeg % 60

print(f'{h}:{min}:{seg}')