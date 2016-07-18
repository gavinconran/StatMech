# naive_spin_dynamics.py
# To simulate the dynamics we use the Metropolis algorithm.
# satisfies detailed balance
# and in the long run - at long times - the two configurations up and down
# will be visited with their corresponding statistical weights: pi_up and pi_down.

import random, math

h = 1.0
beta = 2.0
# probability of moving from an "up" spin to a "down" spin
p = math.exp(- 2.0 * beta * h)
sigma = 1
tmax = 10000000
M_tot = 0
for t in range(tmax):
    if sigma == -1:
        sigma = 1
    elif random.uniform(0.0, 1.0) < p:
        sigma = -1
    M_tot += sigma
print 'magnetization:', M_tot / float(tmax)
# analytic solution
print 'exact result: ', math.tanh(beta * h)
