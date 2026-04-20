n = input()

# aluno.opi@gmail.com

if n.endswith("@gmail.com"):
   print("Dominio Válido")
else:
    print("Dominio Inválido")

# Ou

na = "aluno@gmail.com"

partes = na.split("@")
dominio = partes[-1]

if dominio == "gmail.com":
    print("Válido")
else:
    print("Inválido")