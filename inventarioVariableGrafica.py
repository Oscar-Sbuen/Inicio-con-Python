from numpy import random
import matplotlib.pyplot as plt
T=400
s=50
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
costounitario=0.05
gananciaunitaria=30
lt=[]
lq=[]
while t<T:
    ta=t
    lt.append(ta)
    lq.append(q)
    t=min(tl,tr)
    lt.append(t)
    lq.append(q)
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
print("Ganancia: ",ganancia)
print("Costo: ",costo)
print("Ganancia neta: ",ganancia-costo)
plt.plot(lt,lq)
plt.show()
        
        
        
    
    
