
##ITERATIVE PROOF:
import numpy as np
import scipy as sp
import decimal
import math
# from numba import cuda, jit


sigma =np.array([[[0,1],[1,0]], [[0,-1j],[1j,0]], [[1,0],[0,-1]]], dtype = complex)
# for i in range(3):
#     print(sigma[i])

identity = np.array([[1,0],[0,1]], dtype = complex)
# print(identity)


def mi_generator():
       mx = np.random.normal(0,1,None)
       #mx = 0.1*np.random.random()
       my = np.random.normal(0,1,None)
       #my = 0.1*np.random.random()
       mz = np.random.normal(0,1,None)
       #mz = 0.1*np.random.random()
       arr = np.array([mx, my, mz])
       #print(arr)
       return arr



def positivity_checker(iterations):
    num_fail = 0
    num_succ = 0
    for i in range(iterations):
        m = mi_generator()
        print(m)
        density = (identity)*0.5
        for j in range(3):
            density += (sigma[j]*m[j])*0.5
        #print(density)
 

        w, v = np.linalg.eig(density)

        for k in range(2):
            if(w[k]<0):
                num_fail += 1
                break   

    num_succ = iterations - num_fail 
    prob_fail = (num_fail/(num_fail + num_succ))
    prob_succ = (num_succ/(num_fail + num_succ))
    #print(decimal.Decimal(prob_succ))
    #print(decimal.Decimal(prob_fail))
    #prob_arr = np.array(prob_fail, prob_succ)
    return prob_fail, prob_succ



#@jit(target_backend='cuda') 
def prob_getter(itr,iteration):
    array_p = np.zeros((itr, 2))
    sumf = 0
    sums = 0
    for i in range(itr):

        array_p[i][0], array_p[i][1] = positivity_checker(iteration)
        #print(array_p) 
        sumf += array_p[i][0]
        sums += array_p[i][1]


    for i in range(itr):
        print("fail =",  decimal.Decimal(array_p[i][0]))
        print("success = ", 
              decimal.Decimal(array_p[i][1]))


    # probf = sumf/itr
    # probs = sums/itr

    # print(decimal.Decimal(probf))
    # print(decimal.Decimal(probs))



prob_getter(4,10) ## The number of iterations can be increased.



## ANALYTICAL PROOF:
## We are getting non-zero probabilities of failure because based on the general definition of Density matrix we get the value of 'm' i.e. sqroot(mx2 + my2 + mz2)
## as lying between -1 and 1 while we have considered individual 'mi' as lying between -1 and 1. So, considering uniform probability distribution we can geometrically
## prove that the probability of success is the ratio of vol. of sphere of radius 1 (-1 to 1) and vol. of cube of length = 2 (-1 to 1) in the 'mi' phase space i.e. = pi/6.