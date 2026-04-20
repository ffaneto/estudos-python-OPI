velocidade = 85

if (velocidade <= 80):
    print("Velocidade Normal")
else:
    multa = (velocidade - 80) * 7
    print(f"Multado! Valor: R$ {multa:.2f}")