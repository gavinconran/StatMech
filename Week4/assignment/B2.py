# B2.py
#  Markov-chain program, generalization of markov_pi.py, that samples reasonably well in any dimension d
# works for general d
# Histogram

import random, math, pylab
import numpy as np

# no of dimensions
dimensions = [4, 200]

# function to calculate the volume of a n-dimensional hypersphere
def V_sph(dim):
    return math.pi ** (dim / 2.0) / math.gamma(dim / 2.0 + 1.0)


# for different dimensions
for d in dimensions:
    x = [0.0] * d
    delta = 0.1
    n_trials = 4000000
    n_hits = 0
    old_radius_square = 0.0

    # simulation starting point
    for i in range(n_trials):
        # Instead of modifying all components of x at a time, as we did in markov_pi.py, 
        # modify only one component at each iteration i
        k = random.randint(0, d - 1)
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
    Q = 2 * n_hits / float(n_trials)   
    print "Q4 (approx)= ", Q, " for d: ", d, " dimensions"
    # compute analtic value of Q by computing the ratio of volumes
    Vd = V_sph(d)
    print "Vol = ", Vd, " for ",d, "dimensions"
    Vdminus1 = V_sph(d-1)
    print "Vol = ", Vdminus1, " for ",d-1, "dimensions"
    print "Q(",d,") (analytic): ", Vd/Vdminus1
    print "Error = ", Vd/Vdminus1 - Q







