numero = -1



if (numero == 0):
    print("Nulo")
else:
    if(numero % 2 == 0):
        tipo= "Par"
    else:
        tipo ="Impar"

    if(numero > 0):
        sinal = "Positivo"
    else:
        sinal = "Negativo"

print(f"{tipo} {sinal}")