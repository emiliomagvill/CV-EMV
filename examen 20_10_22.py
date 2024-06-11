rg = int(input("Numero de renglones: "))
cl = int(input("Numero de columnas: "))

import numpy as np
from numpy import random as rd
a = rd.randint(0,10,(rg,cl)) 
print(a)
len_total=0
for r in range(len(a)):
    print(a[r])
    print("sum: ",sum(a[r]))
    print("sum: ",sum(a[r])+sum(a[r]))
    