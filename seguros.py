from random import gauss,random
from math import log

pe=50000      #pago a personal por quincena
tpe=15        #proximo tiempo de pago quincenal
n=10000       #numero de clientes
c=150         #cuota mensual por poliza
lam=1         #tasa de ocurrencia de siniestros
u=35000       #media del pago por siniestro
o=5000        #desviacion estandar de los pagos por siniestro
c0=10000000   #capital inicial
T=365         #tiempo de simulacion en dias
ta=-(1/lam)*log(random()) #tiempo del proximo siniestro
tp=30         #tiempo del proximo pago de los clientes
Cap=c0        #Capitalen el tiempo t
t=0           #tiempo actual
while t<T and min(ta,tp)<T:
    t=min(ta,tp,tpe)
    if t==ta:
        Cap=Cap-gauss(u,o)
        print("Siniestro ","%10.3f"%t,"%10d"%Cap)
        ta=ta-(1/lam)*log(random())
    elif t==tp:
        Cap=Cap+n*c
        print("Pago de polizas ","               ","%10.3f"%t,"%10d"%Cap)
        tp=t+30
    else:
        Cap=Cap-pe
        print("Pago de nomina  ","               ","%10.3f"%t,"%10d"%Cap)
        tpe=tpe+15
print("Ganancia ","%15.2f"%(Cap-c0))
print("Ganancia porcentual ","%10.3f"%(100*(Cap-c0)/c0))

        
