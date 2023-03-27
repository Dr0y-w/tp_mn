import numpy as np
import matplotlib.pyplot as plt


def phi1(x):
    return 1/(1+x) -1/(1-x)
def phi2(x):
    return -2*x/((1+x)*(1-x))

n = 2000
x = np.logspace(-17,-1,n)
e_a = abs(phi1(x)-phi2(x)) 
e_r = abs(phi1(x)-phi2(x))/abs(phi2(x))

plt.loglog(x[e_a>0],e_r[e_a>0])
plt.show()