from math import log2
def question1():
    x=1;p=0
    while (1+x)>1:
        x=x/2
        p=p+1
    u = x
    p = -log2(u)
    return u,p


#test
u,p = question1()
print(f"u :{u}; p :{p}")