from random import random
from math import log
n=100
l_l=1
l_s=2
tl=0
tis=0
ts=tis-(1/l_s)*log(random())
for i in range(n):
    print("%4d"%i,"%8.3f"%tl,"%8.3f"%tis,"%8.3f"%ts)
    tl=tl-(1/l_l)*log(random())
    tis=max(tl,ts)
    ts=tis-(1/l_s)*log(random())
    
