D = int(input())


if (D % 5 == 0):
    pulos = D // 5
    print(f"Chegou com {pulos} pulos")
else:
    sobra = D % 5
    falta = 5 - sobra
    print(f"Não chegou, faltam {falta} cm pro próximo pulo")