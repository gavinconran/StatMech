# C2.py
# Modified from C1.py
# works for general d (d=20) 
# Computes the volume of a n-dimensioanl sphere
# Compares Numerical (Monte carlo) and analytic techniques for the computtaion
# You will need to install prettytable for this to work

import random, math, pylab
import numpy as np
from operator import mul
from prettytable import PrettyTable


# no of dimensions
d=20
trials = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]
n_runs = 10

Avg_Vols = []  # MC Vol
Exacts =   []  # Analytical Vol
Errors = []  # Errors
Diffs = [] #  difference between the Monte Carlo and exact results for V_sph(20)

# function to calculate the volume of a n-dimensional hypersphere
def V_sph_fun(dim):
    return math.pi ** (dim / 2.0) / math.gamma(dim / 2.0 + 1.0)


# for different dimensions
for n_trials in trials:    
    Vol = []
    Vol2 = []
    Ana = []
    Qs = []
    # run simulation 10 times
    for run in range(0, n_runs):
        x = [0.0] * d
        delta = 0.1
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
        Qs.append(Q)
        # compute the volme from this simulation
        V_sph = 2.0 * np.prod(Qs)
        Vol.append(V_sph)
        V_sph2 = V_sph**2
        Vol2.append(V_sph2)
        V_ana = Qs[-1] * V_sph_fun(d)
        Ana.append(V_ana)

    # Compute the Volumes(MC and analtical), error and difference
    Avg_V_sph = sum(Vol) / float(len(Vol))
    Avg_V_sph2 = sum(Vol2) / float(len(Vol2))
    Avg_Ana_V_sph = sum(Ana) / float(len(Ana))
    error = math.sqrt(Avg_V_sph2 - Avg_V_sph**2) / math.sqrt(len(Vol))
    difference = Avg_V_sph - Avg_Ana_V_sph
    

    # Add approx vol, Exact Vol, Error, and difference to appropriate lists 
    Avg_Vols.append(Avg_V_sph)    
    Exacts.append(Avg_Ana_V_sph)
    Errors.append(error)
    Diffs.append(difference)

#print out results
t = PrettyTable(['n_trials', '<V_sph(20)>', 'V_sph(20) exact' , 'error', 'difference'])
for i in range(len(trials)):
    t.add_row([trials[i], Avg_Vols[i], Exacts[i], Errors[i], Diffs[i]])
print t










