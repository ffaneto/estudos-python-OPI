palavra= input()
alvo = "a"
resultado = ""

for letra in palavra:
    if(letra == alvo):
        resultado += "*"
    else:
        resultado += letra


print(resultado)

tamanho = len(palavra)
for i in range(tamanho):
    if(palavra[i] == alvo):
        print(f"Achei um '{alvo}' no indice {i}")