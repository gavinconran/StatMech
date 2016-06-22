# A2.py
# Quantum particle in the harmonic potential, at finite temperature
# Markov-chain Monte Carlo algorithm for a particle in a Gaussian potential, 
# using the Metropolis algorithm for acceptance
# samples positions x according to the probability pi(x) = psi_0(x)^2


import random, math, pylab

def Energy(n):
    return n + 0.5

def psi_n(n, x):
    En = Energy(n) + 0.5
    return (1 / math.pi**0.25) * math.exp(-x**2/float(2)) + En

# Ground state wave function squared
def psi_n_sq(x):
    En = Energy(n) + 0.5
    return ((1 / math.pi**0.25) * math.exp(-x**2/float(2)) + En)** 2


# returns a list of psi values for given x poisition for a given energy state, n
def psi_n_square(x, n):
    if n == -1:
        return 0.0
    else:
        psi = [math.exp(-x ** 2 / 2.0) / math.pi ** 0.25]
        psi.append(math.sqrt(2.0) * x * psi[0])
        for k in range(2, n + 1):
            psi.append(math.sqrt(2.0 / k) * x * psi[k - 1] -
                       math.sqrt((k - 1.0) / k) * psi[k - 2])
        return psi[n] ** 2


# construct waveforms
n_states = 4
grid_x = [i * 0.2 for i in range(-25, 26)]
psi = {}
n=0
beta = 0.2 # 1 # 5
T = 1 / beta # temperatutre, T
delta = 0.1
data = []

for k in range(50000):
    x = random.choice(grid_x)
    x_new = x + random.uniform(-delta, delta)
    
    if random.uniform(0.0, 1.0) <  \
        min(1, (psi_n(x_new, n) / psi_n(x, n))**2):
        #min(1, psi_n_square(x_new, n) / psi_n_square(x, n)):
        x = x_new 

    m = random.randrange(-1, 2, 2)
    n_new = n + m

    if (n_new > 0) and random.uniform(0.0, 1.0) <  \
        min(1, (psi_n(x, n) / psi_n(x, n))**2 * math.exp(-beta*(Energy(n_new-Energy(n))))):
        n = n_new

#modify the program further, and add a move which keeps x fixed and changes n to m = n +/-1. Such a move from (n, x) #to (m = n +/-1, x) should be accepted with the p=min(1, (psi_m(x)/psi_n(x))^2 * exp(-beta*(E_m-E_n)). Moves to m < #0 must be proposed (piles of pebbles!!), but they should always be rejected.


        

    data.append(x)

pylab.hist(data, 100, normed = 'True')
x = [a/float(1000) for a in range(-3000, 3000)]
y = [psi_n_sq(a) for a in x] 
pylab.plot(x, y, c='red', linewidth=2.0)

pylab.title('Theoretical Gaussian distribution $\pi(x)$ and \
    \nnormalized histogram for '+str(len(data))+' samples', fontsize = 18)
pylab.xlabel('$x$', fontsize = 30)
pylab.ylabel('$\pi(x)$', fontsize = 30)
pylab.savefig('plot_markov_gauss_finite_temp.png')
pylab.show()
