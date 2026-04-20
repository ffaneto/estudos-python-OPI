
s = "peixe"
tentativas = 0

while True:
    n = input()
    tentativas +=1

    if (n == s) :
        print("Senha Correta")
        print(f"Tentativas: {tentativas}")
        break

    if(n and n[0] == "p"):
        print("Senha Incorreta - Dica: Você está no caminho certo")

    else:
        print("Senha Incorreta")