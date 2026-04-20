
nome, cpf = input().split()


cpfFinal = cpf[-3:]

if(len(nome) >= 3):
    print(nome[0:3].upper() + cpfFinal)
else:
    nomeComX = (nome + "X").upper()
    print(nomeComX + cpfFinal)
