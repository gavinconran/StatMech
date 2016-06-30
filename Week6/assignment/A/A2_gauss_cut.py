# A2.py
# hit and run
# break up pi(x,y) into a product of one-dimensional distributions. 
# We use the Markov-chain method.
# Markov-chain programs, because the outcome of the move depended on the present configuration
# Nevertheless, a direct-sampling approach was used in the coordinate that was changed.

import random, math, pylab

# returns a Gaussian with unit standard deviation and zero mean, 
# restricted to the interval [-1.0, 1.0]
def gauss_cut():
    while True:
        x = random.gauss(0.0, 1.0)
        if abs(x) <= 1.0:
            return x

oneD_max = 0.5 / math.sqrt(2.0 * math.pi) # 2-D therefore 0.5 rather than 1.0 numerator
alpha = 0.5
nsteps = 1000000
samples_x = []
samples_y = []
x, y = 0.0, 0.0
for step in range(nsteps):
    if step % 2 == 0:
        while True:
            x = gauss_cut() #random.uniform(-1.0, 1.0)
            p = math.exp(-0.5 * oneD_max * x ** 2 - alpha * x ** 4 )
            if random.uniform(0.0, 1.0) < p:
                break
    else:
        while True:
            y = gauss_cut() #random.uniform(-1.0, 1.0)
            p = math.exp(-0.5 * oneD_max * y ** 2 - alpha * y ** 4 )
            if random.uniform(0.0, 1.0) < p:
                break
    samples_x.append(x)
    samples_y.append(y)

pylab.hexbin(samples_x, samples_y, gridsize=50, bins=1000)
pylab.axis([-1.0, 1.0, -1.0, 1.0])
cb = pylab.colorbar()
pylab.xlabel('x')
pylab.ylabel('y')
pylab.title('A2_1')
pylab.savefig('plot_A2_1_GC.png')
pylab.show()
