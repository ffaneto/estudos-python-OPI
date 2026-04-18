# Um carro faz 12km/L
# Distância = Tempo x Velocidade
# Litros = Distância/12

tempo, velocidade = map(int, input().split())

distancia = tempo * velocidade

litros = distancia/12

print(f'Total de combustível gasto: {litros:.3f}')