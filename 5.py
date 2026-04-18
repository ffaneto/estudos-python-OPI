#Exercício 1: Calculando a Força do Kamehameha

#O Kamehameha de Goku tem sua força baseada em seu poder de luta e um fator de concentração. Vamos calcular a força final!

#Problema: Peça ao usuário o poder de luta atual de Goku e um fator de concentração.
# Calcule a força do Kamehameha como (poder_luta * fator_concentracao e exiba o resultado)


print("Poder de luta atual de Goku e um fator de concentração")

poder_luta, fator_concentracao = map(float, input("Coloque em uma linha só os valores: ").split())

result = poder_luta * fator_concentracao

print(f'{poder_luta} * {fator_concentracao} = {result:.2f}')