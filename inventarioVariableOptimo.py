from math import log
from numpy import random
import matplotlib.pyplot as plt
def f(s):
    T=200
    S=150
    q=S
    l_l=0.5
    t=0
    tl=random.exponential(1/l_l)
    tr=20
    rep=30
    v=0
    nv=0
    costo=0
    ganancia=0
    costounitario=0.2
    gananciaunitaria=30
    while t<T:
        ta=t
        t=min(tl,tr)
        costo=costo+(t-ta)*q*costounitario
        if t==tl:
            dem=random.poisson(3)
            if q>=dem:
                q=q-dem
                #print("Llegada ","%10.2f"%tl,"Demanda ",dem,q)
                v=v+dem
                ganancia=ganancia+gananciaunitaria*dem
            else:
                nv=nv+dem-q
                ganancia=ganancia+q*gananciaunitaria
                #print("Venta perdida","%10.2f"%tl,"Demanda ",dem,"Ventas perdidas ",dem-q,"Quedan ",0)
                q=0
            tl=tl+random.exponential(1/l_l)
        else:
            if q<s:
                q=S
            #print("Tiempo de reposición","%10.2f"%tr,q)
            tr=tr+rep
    return ganancia-costo
n=10000
s=20
while s<140:
    suma=0
    for i in range(n):
        suma=suma+f(s)
    print(s,suma/n)
    s=s+10
    
    
        
        
    
    
