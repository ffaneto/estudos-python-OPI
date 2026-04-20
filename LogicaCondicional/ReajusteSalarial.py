salario = 1500


if (salario <= 1500):
    salario += (salario * 0.15)
else:
    salario += (salario * 0.10)

print(f"Novo salario: R$ {salario:.2f}")