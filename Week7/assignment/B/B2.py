# B2.py
# extension of B1.py
# markov_harmonic_bosons.py in 3-D

import random, math, numpy, sys, os
import pylab, mpl_toolkits.mplot3d

def levy_harmonic_path_3d(k):
    x0 = tuple([random.gauss(0.0, 1.0 / math.sqrt(2.0 *
                math.tanh(k * beta / 2.0))) for d in range(3)])
    x = [x0]
    for j in range(1, k):
        Upsilon_1 = 1.0 / math.tanh(beta) + 1.0 / \
                          math.tanh((k - j) * beta)
        Upsilon_2 = [x[j - 1][d] / math.sinh(beta) + x[0][d] /
                     math.sinh((k - j) * beta) for d in range(3)]
        x_mean = [Upsilon_2[d] / Upsilon_1 for d in range(3)]
        sigma = 1.0 / math.sqrt(Upsilon_1)
        dummy = [random.gauss(x_mean[d], sigma) for d in range(3)]
        x.append(tuple(dummy))
    return x

def rho_harm_3d(x, xp):
    Upsilon_1 = sum((x[d] + xp[d]) ** 2 / 4.0 *
                    math.tanh(beta / 2.0) for d in range(3))
    Upsilon_2 = sum((x[d] - xp[d]) ** 2 / 4.0 /
                    math.tanh(beta / 2.0) for d in range(3))
    return math.exp(- Upsilon_1 - Upsilon_2)

# snippet 1: read the configuration from a file (if possible)
# Initial condition
N = 512
T_star = 0.8 #2.5 #0.7
beta = 1.0 / (T_star * N ** (1.0 / 3.0))
filename = 'data_boson_configuration_B2_TStar=%s.txt' % T_star
positions = {}


if os.path.isfile(filename):
    f = open(filename, 'r')
    for line in f:
        a = line.split()
        positions[tuple([float(a[0]), float(a[1]), float(a[2])])] = \
               tuple([float(a[3]), float(a[4]), float(a[5])])
    f.close()
    if len(positions) != N:
        sys.exit('ERROR in the input file.')
    print 'Starting from file', filename
else:
    for k in range(N):
        a = levy_harmonic_path_3d(1)
        positions[a[0]] = a[0]
    print 'Starting from a new configuration'


# Monte Carlo loop
# initialise sampling variables
data_x = []
data_x_cycle_min = []
cycle_min = 10 #9 #8 #7 #6 #5 #4 #3 #2

nsteps = 100000
for step in range(nsteps):
    # move 1: resample one permutation cycle
    boson_a = random.choice(positions.keys())
    perm_cycle = []
    while True:
        perm_cycle.append(boson_a)
        boson_b = positions.pop(boson_a)
        if boson_b == perm_cycle[0]:
            break
        else:
           boson_a = boson_b
    # sample position x
    data_x.append(boson_a[0])    
    k = len(perm_cycle)
    # sample position x if k > cycle_min
    if k > cycle_min:
        data_x_cycle_min.append(boson_a[0])  

    perm_cycle = levy_harmonic_path_3d(k)
    positions[perm_cycle[-1]] = perm_cycle[0]
    for k in range(len(perm_cycle) - 1):
        positions[perm_cycle[k]] = perm_cycle[k + 1]
    # move 2: exchange
    a_1 = random.choice(positions.keys())
    b_1 = positions.pop(a_1)
    a_2 = random.choice(positions.keys())
    b_2 = positions.pop(a_2)
    weight_new = rho_harm_3d(a_1, b_2) * rho_harm_3d(a_2, b_1)
    weight_old = rho_harm_3d(a_1, b_1) * rho_harm_3d(a_2, b_2)
    if random.uniform(0.0, 1.0) < weight_new / weight_old:
        positions[a_1] = b_2
        positions[a_2] = b_1
    else:
        positions[a_1] = b_1
        positions[a_2] = b_2


# create histogram
pylab.hist(data_x, normed=True, bins=100, alpha = 0.75, label='all x')
pylab.hist(data_x_cycle_min, normed=True, bins=100, alpha = 0.75, label='cycle_min x')
list_x = [0.1 * a for a in range (-30, 31)]
list_y = [math.exp(-x**2)/math.sqrt(math.pi) for x in list_x] ### added code
pylab.plot(list_x, list_y, label='analytic')
pylab.legend()
pylab.xlabel('$x$')
pylab.ylabel('$\\pi(x)$ (normalized)')
pylab.title('%s bosonic quantum particles in 3-D \
         \nharmonic trap (T*=%s, N=%i, cycle_min=%s)' % (N, T_star, nsteps, cycle_min))
pylab.xlim(-3.0, 3.0) # this plots the above histogram in the restricted range -3.0 .... 3.0
pylab.savefig('plot_B2_N=%s_Tstar=%s.png' % (N,T_star))
pylab.show()
    
# snippet 2: write configuration on a file
f = open(filename, 'w')
for a in positions:
   b = positions[a]
   f.write(str(a[0]) + ' ' + str(a[1]) + ' ' + str(a[2]) + ' ' +
           str(b[0]) + ' ' + str(b[1]) + ' ' + str(b[2]) + '\n')
f.close()


