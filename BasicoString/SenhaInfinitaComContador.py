s = "python123"
tentativas = 0



while True:
    n = input()
    tentativas +=1

    if(n == s):
        print("Acesso Permitido")
        print(f"Total de tentativas:{tentativas}")
        break
    else:
        print("Senha Incorreta")
