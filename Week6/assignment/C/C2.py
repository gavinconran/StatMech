# C2.py
# extension of B2_levy_harmonic_path.py
# variant levy_harmonic_path.py
# Markov-chain using partial freezing" + "direct sampling

import math, random, pylab


# Step 1: Incorporate a function V_anharm(x, cubic, quartic)
# does not include harmonic part x**2
def V_anharm(x, cubic, quartic):
    pot = cubic * x ** 3 + quartic * x ** 4
    return pot

# This function (which returns a list of N elements) 
# should replace the naive construction for the N elements of naive_harmonic_path                            
def levy_harmonic_path(xstart, xend, dtau, N):
    x = [xstart]
    for k in range(1, N):
        dtau_prime = (N - k) * dtau
        Ups1 = 1.0 / math.tanh(dtau) + \
               1.0 / math.tanh(dtau_prime)
        Ups2 = x[k - 1] / math.sinh(dtau) + \
               xend / math.sinh(dtau_prime)
        x.append(random.gauss(Ups2 / Ups1, \
               1.0 / math.sqrt(Ups1)))
    return x

# It is important to realize that the rho_free part of the free density matrix is no longer in the Metropolis step.
# Therefore, you should replace the harmonic Levy construction of section B2 by the free Levy construction, 
# but new paths should be accepted with the Metropolis algorithm.
def levy_free_path(xstart, xend, dtau, N):
    x = [xstart]
    for k in range(1, N):
        dtau_prime = (N - k) * dtau
        x_mean = (dtau_prime * x[k - 1] + dtau * xend) / \
                 (dtau + dtau_prime)
        sigma = math.sqrt(1.0 / (1.0 / dtau + 1.0 / dtau_prime))
        x.append(random.gauss(x_mean, sigma))
    return x

# Initialise variables
beta = 20.0
N = 100
dtau = beta / N
x = levy_harmonic_path(5.0, 5.0, dtau, N)
data = []
Ncut = N/20
cubic = -1.0
quartic = 1.0 # 0
accept = 0
Weight_old = math.exp(sum(-V_anharm(a, cubic, quartic) * dtau for a in x))

n_steps = 400000
for step in range(n_steps):
    # Step 2: Construct a new path (x_new) between x[0] and x[0], from Levy_free_path.
    x_new = levy_harmonic_path(x[0], x[Ncut], dtau, Ncut) + x[Ncut:]  
    # Step 3: Compute its Trotter weight, the part of the statistical weight not yet taken into account by the path construction
    Weight_new = math.exp(sum(-V_anharm(a, cubic, quartic) * dtau for a in x_new))
    # Step 4: Accept the new path with probability min(1, Weight_new/ Weight_old)
    if random.uniform(0.0, 1.0) < min(1, Weight_new/ Weight_old):
        # Update the Weight_old
        Weight_old = math.exp(sum(-V_anharm(a, cubic, quartic) * dtau for a in x)) + Weight_new
        #print "Weight_old: ", Weight_old
        # Update the path
        x = x_new[:]
        # Wrap the path
        x = x[1:] + x[:1]
        accept += 1
    k = random.randint(0, N - 1)
    data.append(x[k])   

print "accept: ", accept

pylab.hist(data, normed=True, bins=100, label='QMC')
list_x = [0.1 * a for a in range (-30, 31)]
list_y = [math.sqrt(math.tanh(beta / 2.0)) / math.sqrt(math.pi) * \
          math.exp(-x ** 2 * math.tanh(beta / 2.0)) for x in list_x]
pylab.plot(list_x, list_y, label='analytic')
pylab.legend()
pylab.xlabel('$x$')
pylab.ylabel('$\\pi(x)$ (normalized)')

pylab.title('Levy Harmonic Path (Beta=%s, N=%i) ' %(beta, N) + \
            '\nNormalized Histogram (Cubic=%s, Quartic=%s) ' % (cubic, quartic), fontsize = 18)

#pylab.title('levy_free_path (beta=%s, N=%i)' % (beta, N))
pylab.xlim(-2, 2)
pylab.savefig('plot_C2_beta%s.png' % beta)
pylab.show()

