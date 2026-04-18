a , b= input().split()

a , b = int(a), int(b)

print(a ** b)


def primo (n) :
    if (n < 2):
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())

if primo(n):
    print("Primo")
else:
    print("Não primo")

#Se p é primo, então, para qualquer a, a^p - a é divisível por p
# 7 é primo, 1^7 - 1 é divisível por 7
# 1-1 é 0, 0 é divisível por 7

# 2⁷ - 2 é 126. 126/7 é 18.


def testar_fermat(p, limite_a):
    for a in range(1, limite_a + 1):
        calc = a**p - a
        if calc % p == 0:
            print(f"a = {a}: {calc} é divisível por {p}")
        else:
            print(f"a = {a}: {calc} não é divisível")

testar_fermat(100,2)