ticket, val_compra = map(float, input().split())

if (ticket % 2 == 0) :
    val_compra -= (val_compra * 0.15)
elif(ticket % 5 == 0) :
    val_compra -= (val_compra * 0.20)
else:
    val_compra -= (val_compra * 0.05)


print(f'{val_compra:.2f}')

