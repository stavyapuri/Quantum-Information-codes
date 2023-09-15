
import numpy as np
import scipy as sc
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 

step = 1000

y = np.zeros(step)
x = np.zeros(step)

def logneg(p):
    rho = np.matrix([[0.5,0,0,0],[0,0,(-p+0.5),0],[0,(-p+0.5),0,0],[0,0,0,0.5]])
    temp = np.transpose(rho)
    par_rho = np.matrix.conjugate(temp)
    #print(rho)
    #print(par_rho)
    prec = par_rho*rho
    temp2 = sc.linalg.sqrtm((prec))
    l1norm = np.trace((temp2))
    neg = (l1norm - 1/2)
    #print(np.log2((2*neg)+1))
    y[i] = np.log2((2*neg)+1)
    #return np.log2((2*neg)+1)

#p = np.linspace(0, 1, 100)



for i in range(step):
 logneg(i/step)
 x[i] = i/step
  

plt.plot(x, y)
  


plt.show()





