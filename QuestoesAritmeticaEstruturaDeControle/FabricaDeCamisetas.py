#Caixa grande cabe 50 Camisetas
#Caixa média cabe 10 Camisetas
#Caixa pequena cabe 1 Camiseta

# 163 // 50 -> 3 Caixas grandes, porém sobram 13 camisetas
# 13 // 10 -> 1 Caixa média, porém sobram 3 camisetas
# 3 // 1 -> 3 caixas pequenas, sobrando 0 camisetas


total = int(input())

caixaG = total // 50
sobra = total % 50

caixaM = sobra // 10
sobra = sobra % 10

caixaP = sobra // 1
sobra = sobra % 1

print(f"G: {caixaG}, M: {caixaM}, P: {caixaP}")
