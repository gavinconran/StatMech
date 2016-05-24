# C2.py: replaces pi through its best estimate, the mean value <Obs>. 
# Using the estimate <Obs^2> - <Obs>^2.
# Program estimates the mean value of Obs (Obs can be 0 or 4), but also of Obs^2 (which can be 16 or 0)

import random, math
n_trials = 400000
n_hits = 0

ObsTotal = 0.0 # Keeps track of the total sum of Obs
ObsSqTotal = 0.0 # keeps track of the total sum of Obs**2
for iter in range(n_trials):
    x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
    Obs = 0.0
    ObsSq = 0.0
    if x**2 + y**2 < 1.0:
        n_hits += 1
        Obs = 4.0
        ObsSq = 16.0
    ObsTotal += Obs
    ObsSqTotal += ObsSq

ObsSqMean =  ObsSqTotal/ float(n_trials) # computes <Obs**2>
ObsMean = (ObsTotal/ float(n_trials))**2 # Computes <Obs>**2
print 4.0 * n_hits / float(n_trials), math.sqrt(ObsSqMean - ObsMean) 
