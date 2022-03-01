#Correcto
from random import random
from math import log
import matplotlib.pyplot as plt
from statistics import mean,stdev
def F(alfa):
    return (-1/alfa)*log(random())

infi=100000000
alfa=1/50
beta=1/5
n=5
s=3
infi=100000000
disp=s
td=[]
for i in range(n):
    td.append(F(alfa))
tdp=min(td)
tsp=infi
l=0
indicador=0
while indicador==0:
    t=min(tdp,tsp)
    if tdp==tsp:
        print("Cuidado")
    if t==tdp:
        if disp==0:
            indicador=1
            k=td.index(tdp)
        else:
            disp=disp-1
            l=l+1
            k=td.index(tdp)
            td[k]=t+F(alfa)
            if l==1:
                tsp=t+F(beta)
            tdp=min(td)
        print("Des ","%8.3f"%t," Maq ",k,disp,l)
    else:
        l=l-1
        disp=disp+1
        if l>0:
            tsp=t+F(beta)
        else:
            tsp=infi
        print("                               Fin rep ","%8.3f"%t,disp,l)
print(t)
