# A1.py

import random, math

def prob(x):
    s1 = math.exp(-(x + 1.2) ** 2 / 0.72)
    s2 = math.exp(-(x - 1.5) ** 2 / 0.08)
    return (s1 + 2.0 * s2) / math.sqrt(2.0 * math.pi)

delta = 1.11 #20.0 #10.0
nsteps = 100000000
runs = [1, 2, 3, 4]
print 'delta ', delta, ' : nsteps =', nsteps
for run in runs:
    acc_tot = 0
    x = 0.0
    x_av = 0.0
    for step in xrange(nsteps):
        xnew = x + random.uniform(-delta, delta)
        if random.uniform(0.0, 1.0) < prob(xnew) / prob(x):
            x = xnew
            acc_tot += 1
        x_av += x

    print 'global acceptance ratio:', acc_tot / float(nsteps)
    print 'run ', run, 'global acceptance ratio:', acc_tot / float(nsteps), ' : <x> =', x_av / float(nsteps)
