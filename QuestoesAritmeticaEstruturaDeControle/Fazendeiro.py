# // -> RESPOSTA (Quantas semanas/horas/notas cabem?)
# %  -> SOBRA (O que ficou de fora da divisão?)

ovos= int(input())

caixas = ovos // 12
sobra = ovos % 12

print(caixas, sobra)