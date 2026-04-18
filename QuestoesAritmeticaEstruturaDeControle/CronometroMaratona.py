total = int(input())

H = total // 3600
sobra = total % 3600

M = sobra // 60
sobra = sobra % 60

S = sobra

print(f"{H}:{M}:{S}")