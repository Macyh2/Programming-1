﻿eggs = int(input("Number of Eggs Purchased:"))
dozens = eggs/12
remainder = eggs%12
price = 0.0
cost = 0.0

if dozens > 0 and dozens < 4:
    price = 0.5
elif dozens >= 4 and dozens < 6:
    price = 0.45
elif dozens >= 6 and dozens < 11:
    price = 0.4
elif dozens >= 11:
    price = 0.35

dozensp = ((dozens * price) / dozens)
cost = (dozens * price)
realcost = cost + ((eggs * price) - remainder)
print("Total cost is $" + str(round(realcost,2)))
input()