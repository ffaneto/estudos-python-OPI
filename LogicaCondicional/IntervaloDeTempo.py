# Se o jogo começa as 22:00 e termina as 02:00, ele durou 4 horas, por quê?
# Porque de 22:00 até 00:00 são 2 horas, e de 00:00 até 02:00 são 2 horas
# Logo, 2h + 2h = 4 horas
# 00:00 é o ponto inicial?
# Se HoraInicial < HoraFinal, então print(HoraFinal - HoraInicial)
# Se HoraFinal > HoraInicial, então print(24 - HoraInicial) + HoraFinal

hI, hF = map(int, input().split())

if(hF > hI):
    print(hF - hI)
else:
    print((24 - hI) + hF)