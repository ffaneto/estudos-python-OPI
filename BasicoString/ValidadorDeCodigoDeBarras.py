cod = input()

#AABBCCCC

print("Estado:",cod[0:2])
print("Tipo:",cod[2:4])
print("Preço:",cod[4:8])
preco = cod[4:8]
print("Preço Invertido:", preco[::-1])