from math import log
from random import random

T=10
l_l=1
l_s=2
t=0
infi=1000000000
ts=infi
tl=0
l=0
while min(tl,ts)<T:
    t=min(tl,ts)
    if tl<=ts:
        l=l+1
        print("%10.2f"%tl,l)
        tl=t-(1./l_l)*log(random())
        if l==1:
            ts=t-(1./l_s)*log(random())
    else:
        l=l-1
        print("               ","%10.2f"%ts,l)
        if l>0:
            ts=t-(1./l_s)*log(random())
        else:
            ts=infi
            

    

