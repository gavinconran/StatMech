# A2.py
# Quantum particle in the harmonic potential, at finite temperature
# Markov-chain Monte Carlo algorithm for a particle in a Gaussian potential, 
# using the Metropolis algorithm for acceptance
# samples positions x according to the probability pi(x) = psi_0(x)^2

import random, math, pylab

# Used fros STEP 1
# n state wave function
def psi_n(x, n):
    return (1 / math.pi**0.25) * math.exp(-x**2/float(2)) #math.exp(-beta * n)   #

# used for STEP 2
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

# Compute Energy of a state n
def E_n(n):
    return n + 0.5

# Compute Exact Quantum Probability Distribution
def prob_quant(x, Beta):
    return math.sqrt(math.tanh(Beta/float(2)) / math.pi) * math.exp(- x**2 * math.tanh(Beta/float(2))) 

# Compute Exact Classical Probability Distribution
def prob_classic(x, Beta):
    return math.sqrt(Beta/ (2*math.pi)) * math.exp(-Beta * x**2/float(2)) 

# Helper function for A2 step 1
def step1(x_new, x, n, Beta):
    return min(1, (psi_n_square(x_new, n) / psi_n_square(x, n))) #**2

# Helper function for A2 step 2
def step2(psi_x_n_new_sq, x_new, x, n_new, n, Beta):
    return min(1, (psi_x_n_new_sq / psi_n_square(x, n)) * math.exp(-Beta * (E_n(n_new) - E_n(n))))


# Beta is proportional to 1 / T
BetaList = [5, 1 , 0.2] 
n_trials = 10000000
for Beta in BetaList:
    # Initialise variables
    x = 0.0
    delta = 0.1
    n = 2
    data = []
    # apply markov-chain Monte carlo sampling with Metropolis acceptance
    # to approximate the finte temperature quantaum probability distribution
    for k in range(n_trials):
        x_new = x + random.uniform(-delta, delta)

        # step 1: move (n,x) to (n, x')
        if random.uniform(0.0, 1.0) < step1(x_new, x, n, Beta):
            x = x_new 
            #print "step 1"

        # step 2:
        m = random.randrange(-1, 2, 2)
        n_new = n + m
        

#Notice that this function returns 0 when n=-1. This is useful to simplify the acceptance probability for the n-changing move, #since we want to reject all moves that go from n=0 to n=-1)
        psi_x_n_new_sq =  psi_n_square(x, n_new)
        #if n == 0 and  and psi_x_n_new_sq > 0 and 
        if not(n == 0 and psi_x_n_new_sq == 0):
            if random.uniform(0.0, 1.0) <  \
                           step2(psi_x_n_new_sq, x_new, x, n_new, n, Beta):    
                n = n_new
                #print "step 2"
        #print "n = ", n
        data.append(x)

    # Create Graphic
    pylab.figure()
    pylab.hist(data, 100, normed = 'True')
    x = [a/float(1000) for a in range(-6000, 6000)]
    # Plot exact Quantum Probability Distribution
    y_quant = [prob_quant(a, Beta) for a in x] 
    pylab.plot(x, y_quant, c='red', linewidth=2.0, label='Quantum')
    # Plot exact Classical Probability Distribution
    y_classic = [prob_classic(a, Beta) for a in x] 
    pylab.plot(x, y_classic, c='green', linewidth=2.0, label="Classical")
    pylab.title('Normalized histogram for '+str(len(data))+' samples\
        \nfor Beta = ' +str(Beta), fontsize = 18)
    pylab.xlabel('$x$', fontsize = 20)
    pylab.ylabel('$\pi(x)$', fontsize = 20)
    pylab.legend(loc='best')
    pylab.savefig('%d_plot_finite_Temp_B=%d.png' % (n_trials, Beta))
    
#pylab.show()
