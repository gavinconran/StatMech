# A1.py
# DIRECT SAMPLING REJECTION ALGO
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

y_max = 0.5 / math.sqrt(2.0 * math.pi) # 2-D therefore 0.5 rather than 1.0 numerator
alpha = 0.5  #0.005 #1.0 #0.5
nsamples = 1000000
samples_x = []
samples_y = []


for sample in xrange(nsamples):
    while True:
        x = gauss_cut() #random.uniform(-1.0, 1.0)
        y = gauss_cut() #random.uniform(-1.0, 1.0)
        # adjust p
        #p = math.exp((-0.5 * y_max  *(x ** 2 + y ** 2) - alpha * (x ** 4 + y ** 4)) )
        p = math.exp((- alpha * (x ** 4 + y ** 4)) )
        if random.uniform(0.0, 1.0) < p:
            break
    samples_x.append(x)
    samples_y.append(y)

# plot a 2-D histogram using the hexbin function
pylab.hexbin(samples_x, samples_y, gridsize=50, bins=1000)
pylab.axis([-1.0, 1.0, -1.0, 1.0])
cb = pylab.colorbar()
pylab.xlabel('x')
pylab.ylabel('y')
pylab.title('A1_1_GC')
pylab.savefig('plot_A1_1_GC.png')
pylab.show()
