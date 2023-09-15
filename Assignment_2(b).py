
import numpy as np
import scipy as sc
from matplotlib import pyplot as plt
import warnings
import math
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 

step = 1000


y = np.zeros(step)
x = np.zeros(step)
val = np.ones(step)

def logneg(p,a):
    rho = np.matrix([[(1-p)/4,0,0,(p/2)*math.sin(a)],[0,(((1-p)/4)+p*(math.cos(a/2)*math.cos(a/2))),0,0],[0,0,(((1-p)/4)+p*(math.sin(a/2)*math.sin(a/2))),0],[(p/2)*math.sin(a),0,0,(1-p)*0.25]])
    temp = np.transpose(rho)
    par_rho = rho.getH()
    
    #print(rho)
    #print(par_rho)
    prec = par_rho*rho
    temp2 = sc.linalg.sqrtm((prec))
    l1norm = np.trace((temp2))
    neg = (l1norm - 1)/2
    #print(np.log2((2*neg)+1))
    #y[i] = neg
    y[i] = np.log2((2*neg)+1)
    #return np.log2((2*neg)+1)





for i in range(step):
 logneg(i/step,1)
 x[i] = i/step
 
plt.plot(x, y)
  


plt.show()
