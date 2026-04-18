n = int(input())

dias = ["domingo","segunda","terca","quarta","quinta","sexta","sabado"]

i = (n + 1) % 7

print(dias[i])