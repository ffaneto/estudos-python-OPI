nome = "python"

print(nome[0]) # Primeiro caractere da lista

print(nome[-1]) # Último caractere da lista

print(nome[0:2]) # Pega os caracteres desse intervalo, o Início é INCLUSIVO e o Fim é EXCLUSIVO

# | P | Y | T | H | O | N |
# 0   1   2   3   4   5   6
# ^       ^
# |       |
# Quando tu pede nome[0:2], tu tá pegando nesse intervalo
# E nesse intervalo de 0 até 2, as letras são P e Y
# O "2" funciona como ponto de parada

# Se você faz [0:2], basta subtrair o fim pelo início (2−0=2)
# para saber que você vai receber exatamente 2 caracteres.
# Se o 2 fosse incluído, você receberia 3 caracteres, e a conta ficaria sempre "bagunçada" com um +1

# Se você quer dividir uma palavra no meio e depois juntar, os índices se encaixam perfeitamente

pt1 = nome[0:2]
pt2 = nome[2:6]

result = pt1 + pt2

print(result) # python

# O índice 2 termina uma e começa a outra.
# Se o 2 fosse incluído na primeira, a letra 'T' apareceria duplicada

a = "Estudar"

print(a[0:4])

print(a.lower())
print(a.upper())
print(nome.title())