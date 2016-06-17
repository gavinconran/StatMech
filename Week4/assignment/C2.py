# C1.py
# Modified from B2.py
# works for general d
# Computes the volume of a n-dimensioanl sphere

import random, math, pylab
import numpy as np
from operator import mul


# no of dimensions
dd=20
trials = [1, 10, 100, 1000, 10000]
n_runs = 10
delta = 0.1

# function to calculate the volume of a n-dimensional hypersphere
def V_sph(dim):
    return math.pi ** (dim / 2.0) / math.gamma(dim / 2.0 + 1.0)


# for different dimensions
for t in trials:
    print "trial = ", t
    
    for r in range(0, n_runs):
        print "run = ", r
        x = [0.0] * dd
        n_hits = 0
        old_radius_square = 0.0
        Qs = []
        Vol = []
        Vol2 = []
        Ana=[]
        # simulation starting point
        for i in range(t):
            print "i = ", i
            # Instead of modifying all components of x at a time, as we did in markov_pi.py, 
            # modify only one component at each iteration i
            k = random.randint(0, dd - 1)
            x_old_k = x[k]
            x_new_k = x_old_k + random.uniform(-delta, delta)
    
            new_radius_square = old_radius_square + x_new_k ** 2 - x_old_k ** 2
            # check to see if the pebble will still be in the sphere after next throw
            if (0.0 <= new_radius_square and new_radius_square <= 1.0):
                x[k] = x_new_k  # set x[k] to new value of x_new_k
                old_radius_square = new_radius_square # update old_radius_square
        
            alpha = random.uniform(-1.0, 1.0)     
            if (new_radius_square + alpha**2 < 1.0): 
                n_hits += 1

        # print <Q_4>, the average value
        # this is the ratio of the sphere volume for d=4 to the sphere volume for d=3  
        Q = 2 * n_hits / float(t)   
        Qs.append(Q)
    

    # compute and print approxiate and exact values for the volume of a 200-d unit sphere
    print "Approx. V_sph(",dd,"): ", 2.0 * np.prod(Qs)
    print "Approx. V_sph2(",dd,"): ", (2.0 * np.prod(Qs))**2
    print "Exact V_sph(",dd,"): ", Qs[-1] * V_sph(dd)


"""
pylab.plot(dimensions, Ana, c='red', linewidth=2.0, label='Analytic')
pylab.plot(dimensions, Vol, c='blue', linewidth=2.0, label='Monte Carlo')
pylab.title('$Vol(d)$ $versus$ $dimension$', fontsize = 25)
pylab.xlabel('$Dimension$', fontsize = 20)
pylab.ylabel('$Vol(d)$', fontsize = 20)
pylab.yscale('log')
pylab.legend(loc='upper right')
pylab.savefig('C2_d=%d.png' %dd) 
pylab.show()
"""







