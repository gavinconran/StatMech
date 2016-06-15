# Direct Sampling Rejection Algorithm
# CUTS off the tails of the distribution
# Not a problem for a Gaussian distrubution as as x -> 0 then f(x) -> 0 (convergence)

import random, math

y_max = 1.0 / math.sqrt(2.0 * math.pi)
x_cut = 5.0
n_data = 1000
n_accept = 0
while n_accept < n_data:
    y = random.uniform(0.0, y_max)
    x = random.uniform(-x_cut, x_cut)
    # calculate pi(x) using Gauss PDF and chech ti accept or not
    # If y(x) below PDF accept
    if y < math.exp( - x **2 / 2.0)/math.sqrt(2.0 * math.pi): 
        n_accept += 1
        print x
