# implements exact recursion reeelation for the hermite polynomials
# Solves Schroinger equation, i.e. returns the function Psi(x) for values of x

import math, pylab

# construct waveforms
n_states = 4
grid_x = [i * 0.2 for i in range(-25, 26)]
psi = {}
# for each value of x in grid_x
# compute for each of the Energy levels from 0 to n_states-1
# store results in a directionary
# Each key of dictionary is a point x on the grid and
# the value of each element in the dictionary is a list of the computed Enery levels 
for x in grid_x:
    psi[x] = [math.exp(-x ** 2 / 2.0) / math.pi ** 0.25]  # ground state
    psi[x].append(math.sqrt(2.0) * x * psi[x][0])         # first excited state
    # other excited states (through recursion for the Hermite polynomials):
    for n in range(2, n_states):
        psi[x].append(math.sqrt(2.0 / n) * x * psi[x][n - 1] -
                      math.sqrt((n - 1.0) / n) * psi[x][n - 2])
for n in range(n_states):
    print 'level %i:' % n, [psi[x][n] for x in grid_x]

## Plot Psi(x)
x = grid_x
y = [psi[p][0] for p in psi.keys()] 
pylab.plot(x, y, 'k', lw=1.5)
y = [psi[p][1] for p in psi.keys()] 
pylab.plot(x, y, 'b', lw=1.5)
y = [psi[p][2] for p in psi.keys()] 
pylab.plot(x, y, 'r', lw=1.5)
y = [psi[p][3] for p in psi.keys()] 
pylab.plot(x, y, 'g', lw=1.5)
pylab.show()


