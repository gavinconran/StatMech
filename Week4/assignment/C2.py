# C1.py
# Modified from B2.py
# works for general d
# Computes the volume of a n-dimensioanl sphere
# Compares Numerical (Monte carlo) and analytic techniques for the computtaion

import random, math, pylab
import numpy as np
from operator import mul
from prettytable import PrettyTable


# no of dimensions
dd=20
dimensions = range(1, dd)
n_runs = 10
trials = [1, 10, 100, 1000, 10000]

## trial lists
Avg_Vols = []  # MC/Numerical Vol
Exacts =   []  # Analytical Vol
Errors = []  # Errors
Diffs = [] #  difference between the Monte Carlo and exact results for V_sph(20)


# function to calculate the volume of a n-dimensional hypersphere
def V_sph_fun(dim):
    return math.pi ** (dim / 2.0) / math.gamma(dim / 2.0 + 1.0)


for n_trials in trials:    
    Vol = []
    Vol2 = []
    Avg_Q = []
    # for different dimensions
    for d in dimensions:
        delta = 0.1
        
        Qs = []
        for i in range(0, n_runs):
            x = [0.0] * d
            n_hits = 0
            old_radius_square = 0.0

            # simulation starting point
            for j in range(0, n_trials):
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
            Qs.append(Q)

        # add the average of all Q in Qs to Avg_Q  
        Avg_Q.append(np.mean(Qs))
    # Compute the Volumes(MC and analtical), error and difference for this trial
    # Munerical Volume
    V_sph = 2.0 * np.prod(Avg_Q)
    Avg_Vols.append(V_sph)
    V_sph2 = V_sph**2

    # Error of Numerical Volume coputation
    error = math.sqrt(V_sph2) / math.sqrt(n_runs)
    # Analytical Volume
    Ana_V_sph =V_sph_fun(dd)
    # Difference between Numerical and Analytical Volumes
    difference = V_sph - Ana_V_sph

    # Add approx vol, Exact Vol, Error, and difference to appropriate trial lists    
    Exacts.append(Ana_V_sph)
    Errors.append(error)
    Diffs.append(difference)
   
#print out results
t = PrettyTable(['n_trials', '<V_sph(20)>', 'V_sph(20) exact' , 'error', 'difference'])
for i in range(len(trials)):
    t.add_row([trials[i], Avg_Vols[i], Exacts[i], Errors[i], Diffs[i]])
print t














