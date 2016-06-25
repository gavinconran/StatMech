# A1.py
# Markov-chain Monte Carlo algorithm for a particle in a Gaussian potential, 
# using the Metropolis algorithm for acceptance
# samples positions x according to the probability pi(x) = psi_0(x)^2


import random, math, pylab

# Ground state wave function squared
def psi_0_sq(x):
    return ((1 / math.pi**0.25) * math.exp(-x**2/float(2)))** 2

x = 0.0
delta = 0.1
data = []
for k in range(5000000):
    x_new = x + random.uniform(-delta, delta)
    if random.uniform(0.0, 1.0) <  \
         psi_0_sq(x_new) / psi_0_sq(x):
        x = x_new 
    data.append(x)

pylab.hist(data, 100, normed = 'True', label = "Monte Carlo")
x = [a/float(1000) for a in range(-3000, 3000)]
y = [psi_0_sq(a) for a in x] 
pylab.plot(x, y, c='red', linewidth=2.0, label = "Quantum")
pylab.title('Theoretical Gaussian distribution $\pi(x)$ and \
    \nnormalized histogram for '+str(len(data))+' samples', fontsize = 18)
pylab.xlabel('$x$', fontsize = 30)
pylab.ylabel('$\pi(x)$', fontsize = 30)
pylab.xlim(-2.0, 2.0)
pylab.legend(loc='best')
pylab.savefig('plot_markov_gauss_ground_state.png')
pylab.show()
