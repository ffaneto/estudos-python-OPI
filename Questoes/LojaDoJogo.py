m = int(input())

bauOuro = m // 500
sobra = m % 500

bauPrata = sobra // 100
carteira = sobra % 100

print(f'{bauOuro}, {bauPrata}, {carteira}')