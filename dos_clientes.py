from random import random
from math import log
n=100
l_l=1
l_sa=0.7
l_sb=0.2
ia=0
ib=0
tl=0
if random()<0.5:
    tisa=0
    tsa=tisa-(1/l_sa)*log(random())
    ia=1
else:
    tisb=0
    tsb=tisb-(1/l_sb)*log(random())
    ib=1

for i in range(n):
    if ia==0 and ib==0:
        if random()<0.5:
            tisa=tl
            tsa=tisa-(1/l_sa)*log(random())
            ia=1
            print("%8.3f"%tl,"%8.3f"%tisa," por a","%8.3f"%tsa)
            tl=tl-(1/l_l)*log(random())
        else:
            tisb=tl
            tsb=tisb-(1/l_sb)*log(random())
            ib=1
            print("%8.3f"%tl,"%8.3f"%tisb," por b","%8.3f"%tsb)
            tl=tl-(1/l_l)*log(random())
    if ia==0 and ib==1:
        tisa=tl
        tsa=tisa-(1/l_sa)*log(random())
        ia=1
        print("%8.3f"%tl,"%8.3f"%tisa," por a","%8.3f"%tsa)
        tl=tl-(1/l_l)*log(random())
    if ia==1 and ib==0:
        tisb=tl
        tsb=tisb-(1/l_sb)*log(random())
        ib=1
        print("%8.3f"%tl,"%8.3f"%tisb," por b","%8.3f"%tsb)
        tl=tl-(1/l_l)*log(random())
    if ia==1 and ib==1:
        tt=min(tsa,tsb)
        if tt==tsa:
            tisa=tt
            tsa=tisa-(1/l_sa)*log(random())
            print("%8.3f"%tl,"%8.3f"%tisa," por a","%8.3f"%tsa)
            tl=tl-(1/l_l)*log(random())
        else:
            tisb=tt
            tsb=tisb-(1/l_sb)*log(random())
            print("%8.3f"%tl,"%8.3f"%tisb," por b","%8.3f"%tsb)
            tl=tl-(1/l_l)*log(random())
        
    
    
