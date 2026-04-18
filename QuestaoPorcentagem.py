# Problema: Peça ao usuário o poder de luta inicial de Goku e a porcentagem de aumento
# Calcule o novo poder de luta e exiba o resultado.

print("Poder de luta inicial de Goku e a porcentagem de aumento (Ex.: 10 para 10%)")

poder_inicial = input()
percentual_aumento = input()

poder_inicial_flt = float(poder_inicial)
percentual_aumento_flt = float(percentual_aumento)

# Calc

aumento = poder_inicial_flt * (percentual_aumento_flt /100)
novo_poder = poder_inicial_flt + aumento

print(f'{novo_poder}')
