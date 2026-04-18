print("Salário base do Mestre Kame e o valor do bônus em porcentagem (Ex.: 20 = 20% = 0.2)")

sal = input()
bon = input()

sal_flt = float(sal)
bon_flt = float(bon)

aum = sal_flt * (1 + (bon_flt/100))

print(f'{aum:.2f}')