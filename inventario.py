
from math import log
from random import random,seed
#inventario

T=300
s=10
S=20
q=20
l_l=0.5
t=0
tl=-(1/l_l)*log(random())
tr=20
rep=30
v=0
nv=0
costo=0
ganancia=0
costounitario=0.05
gananciaunitaria=40
while min(tl,tr)<T:
    ta=t
    t=min(tl,tr)
    costo=costo+(t-ta)*q*costounitario
    if t==tl:
        if q>0:
            q=q-1
            print("Llegada","%10.2f"%tl,q)
            v=v+1
            ganancia=ganancia+gananciaunitaria
        else:
            print("Llegada","%10.2f"%tl,q,"    Venta perdida")
            nv=nv+1
        tl=tl-(1/l_l)*log(random())
        
    else:
        if q<s:
            q=S
        print("Tiempo de reposición","%10.2f"%tr,q)
        tr=tr+rep
print("Ganancia: ",ganancia)
print("Costo: ",costo)
print("Ganancia neta: ",ganancia-costo)
print("Número de articulos no vendidos ",nv,nv*gananciaunitaria)
        
        
        
    
    
