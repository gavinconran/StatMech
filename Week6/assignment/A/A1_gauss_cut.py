# A1.py
# part 1: proposes uniformly distributed configurations
# part 2: accepts these configurations with the 
# mixed harmonic and quartic weight pi(x,y)
# Produces a 2-D histogram

import random, math, pylab

# returns a Gaussian with unit standard deviation and zero mean, 
# restricted to the interval [-1.0, 1.0]
def gauss_cut():
    while True:
        x = random.gauss(0.0, 1.0)
        if abs(x) <= 1.0:
            return x

y_max = 1.0 / math.sqrt(2.0 * math.pi)
alpha = 0.5  #0.005 #1.0 #0.5
nsamples = 1000000
samples_x = []
samples_y = []


for sample in xrange(nsamples):
    while True:
        x = gauss_cut() #random.uniform(-1.0, 1.0)
        y = gauss_cut() #random.uniform(-1.0, 1.0)
        # adjust p
        p = math.exp((-0.5 *(x ** 2 + y ** 2) - alpha * (x ** 4 + y ** 4)) * y_max )
        if random.uniform(0.0, 1.0) < p:
            break
    samples_x.append(x)
    samples_y.append(y)

"""
while n_accept < n_data:
    y = random.uniform(0.0, y_max)
    x = random.uniform(-x_cut, x_cut)
    # calculate pi(x) using Gauss PDF and chech ti accept or not
    # If y(x) below PDF accept
    if y < math.exp( - x **2 / 2.0)/math.sqrt(2.0 * math.pi): 
        n_accept += 1
        print x
"""

# plot a 2-D histogram using the hexbin function
pylab.hexbin(samples_x, samples_y, gridsize=50, bins=1000)
pylab.axis([-1.0, 1.0, -1.0, 1.0])
cb = pylab.colorbar()
pylab.xlabel('x')
pylab.ylabel('y')
pylab.title('A1_1_GC')
pylab.savefig('plot_A1_1_GC.png')
pylab.show()
