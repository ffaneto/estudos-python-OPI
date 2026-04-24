n = int(input())

p_raw, c , q_raw = input().split()

p = int(p_raw)
q = int(q_raw)

if (c == "+"):
    res = p + q
else:
    res = p * q

if (res > n):
    print("OVERFLOW")
else:
    print("OK")