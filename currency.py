pesos = int(input('What do you have left in pesos? '))
soles = int(input('What do you have left in soles? '))
reais = int(input('What do you have left in reais? '))

total = (pesos * 0.00024) + (soles * 0.26) + (reais * 0.18)

dollars = round(total,2)

print(f'You have USD {dollars} left.')