salario = float(input("Digite seu salário: "))
percentual = float(input("Digite o percentual de doação: "))

doacao = (salario * percentual) / 100

print(f"Você deve doar {doacao:.2f}")