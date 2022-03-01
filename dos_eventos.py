from random import expovariate,random
infi=1000000
l_l=2
l_sa=.9
l_sb=.8
T=100
t=0
l=0
tl=expovariate(l_l)
tsa=infi
tsb=infi
while min(tl,tsa,tsb)<T:
    t=min(tl,tsa,tsb)
    if t==tl:
        l=l+1
        print("%10.3f"%t,l)
        tl=tl+expovariate(l_l)
        if l==1:
            if random()<0.5:
                tsa=t+expovariate(l_sa)
            else:
                tsb=t+expovariate(l_sb)
        if l==2:
            if tsa<infi:
                tsb=t+expovariate(l_sb)
            else:
                tsa=t+expovariate(l_sa)
    elif t==tsa:
        l=l-1
        print("                ","%10.3f"%t," por a",l)
        if l>1:
            tsa=t+expovariate(l_sa)
        else:
            tsa=infi
    else:
        l=l-1
        print("                ","%10.3f"%t," por b",l)
        if l>1:
            tsb=t+expovariate(l_sb)
        else:
            tsb=infi
        
            
