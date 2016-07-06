# A2_2.py
# two bosonic quantum particles in a one-dimensional harmonic trap (as in Section A1, particles do not interact with each other). 
# Program samples their positions from levy_harmonic_path(k), with k=1 or k=2, 
# and proposes to change the permutation structure.


import math, random, pylab
import numpy as np

def levy_harmonic_path(k, beta):
    x = [random.gauss(0.0, 1.0 / math.sqrt(2.0 * math.tanh(k * beta / 2.0)))]
    if k == 2:
        Ups1 = 2.0 / math.tanh(beta)
        Ups2 = 2.0 * x[0] / math.sinh(beta)
        x.append(random.gauss(Ups2 / Ups1, 1.0 / math.sqrt(Ups1)))
    return x[:]

def rho_harm_1d(x, xp, beta):
    Upsilon_1 = (x + xp) ** 2 / 4.0 * math.tanh(beta / 2.0)
    Upsilon_2 = (x - xp) ** 2 / 4.0 / math.tanh(beta / 2.0)
    return math.exp(- Upsilon_1 - Upsilon_2)

def z(beta):
    return 1.0 / (1.0 - math.exp(- beta))

def pi_two_bosons(x, beta):
    pi_x_1 = math.sqrt(math.tanh(beta / 2.0)) / math.sqrt(math.pi) *\
             math.exp(-x ** 2 * math.tanh(beta / 2.0))
    pi_x_2 = math.sqrt(math.tanh(beta)) / math.sqrt(math.pi) *\
             math.exp(-x ** 2 * math.tanh(beta))
    weight_1 = z(beta) ** 2 / (z(beta) ** 2 + z(2.0 * beta))
    weight_2 = z(2.0 * beta) / (z(beta) ** 2 + z(2.0 * beta))
    pi_x = pi_x_1 * weight_1 + pi_x_2 * weight_2
    return pi_x

def z(beta):
    return 1.0 / (1.0 - math.exp(- beta))

# Initialise variables
list_beta = np.arange(0.1, 5.1, 0.1)  #2.0
nsteps = 1000
low = levy_harmonic_path(2, list_beta[0])
high = low[:]
data = []
fract_one_cycle_sim = []
fract_two_cycle_sim = []

# start simulation
for beta in list_beta:
    prob_one_cycle = 0
    prob_two_cycle = 0
    for step in xrange(nsteps):
        # move 1: sample permutations
        # same cycle
        if low[0] == high[0]:
            k = random.choice([0, 1])
            low[k] = levy_harmonic_path(1, beta)[0]
            high[k] = low[k]
            # increase count of same cycle
            prob_two_cycle += 1
        else:
            low[0], low[1] = levy_harmonic_path(2, beta)
            high[1] = low[0]
            high[0] = low[1]
            # incresae count of two cycles
            prob_one_cycle += 1
        data += low[:]
        # move 2: sample positions
        weight_old = (rho_harm_1d(low[0], high[0], beta) *
                  rho_harm_1d(low[1], high[1], beta))
        weight_new = (rho_harm_1d(low[0], high[1], beta) *
                  rho_harm_1d(low[1], high[0], beta))
        # move 2 is accepted/rejected with a probability based on the harmonic off-diagonal density matrix.
        if random.uniform(0.0, 1.0) < weight_new / weight_old:
            high[0], high[1] = high[1], high[0]
    # append fract lists with respective counts
    # These two numbers should sum up to one (prob_one_cycle+prob_two_cycle=1)
    fract_one_cycle_sim.append(prob_one_cycle / float(nsteps))
    fract_two_cycle_sim.append(prob_two_cycle / float(nsteps))


# Analytic
# each boson forms a single cycle
fract_two_cycles = [z(beta) ** 2 / (z(beta) ** 2 + z(2.0 * beta)) for beta in list_beta]
# bosons are on the same cycle
fract_one_cycle = [z(2.0 * beta) / (z(beta) ** 2 + z(2.0 * beta)) for beta in list_beta]


# create chart
pylab.plot(list_beta, fract_one_cycle_sim, label='1-cycle prob')
pylab.plot(list_beta, fract_two_cycle_sim, label='2-cycle prob')

pylab.plot(list_beta, fract_one_cycle, label='1-cycle analytic')
pylab.plot(list_beta, fract_two_cycles, label='2-cycle analytic')
pylab.legend()
pylab.xlabel('$Beta$')
pylab.ylabel('$\\pi (perm)$')
pylab.title('Permutation probabilities of two bosonic quantum particles \
         \nin 1-D harmonic trap (N=%i)' % (nsteps))
pylab.xlim(0, 5)
pylab.savefig('plot_A2_2_steps%s.png' % nsteps)
pylab.show()









