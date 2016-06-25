# C1.py
# computes density matrix for anharmonic oscillator
# Plots chart with approximate and exact probability distribution function (PDF)

import math, numpy, pylab

# returns anharmonic potential
def V(x, cubic, quartic):
    return x ** 2 / 2.0 + cubic * x ** 3 + quartic * x ** 4


# Free off-diagonal density matrix
def rho_free(x, xp, beta):
    return (math.exp(-(x - xp) ** 2 / (2.0 * beta)) /
            math.sqrt(2.0 * math.pi * beta))

# anharmonic density matrix in the Trotter approximation (returns the full matrix)
def rho_anharmonic_trotter(grid, beta, cubic, quartic):
    return numpy.array([[rho_free(x, xp, beta) * \
                         numpy.exp(-0.5 * beta * V(x, cubic, quartic)) * \
                         numpy.exp(-0.5 * beta * V(xp, cubic, quartic)) \
                         for x in grid] for xp in grid])

# Compute Exact Quantum Probability Distribution
def prob_quant(x, Beta):
    return math.sqrt(math.tanh(Beta/float(2)) / math.pi) * math.exp(- x**2 * math.tanh(Beta/float(2))) 


# Initialise variables
x_max = 5 # 5 #50.0
nx = 100
dx = 2.0 * x_max / (nx - 1)
x = [i * dx for i in range(-(nx - 1) / 2, nx / 2 + 1)] 
beta_tmp = 2.0 ** (-8)                   # initial value of beta (power of 2)
beta     = 2.0 ** 2                           # actual value of beta (power of 2)
cubic = -1.0
quartic = 1.0 # 0
rho = rho_anharmonic_trotter(x, beta_tmp, cubic, quartic)  # density matrix at initial beta
while beta_tmp < beta:
    rho = numpy.dot(rho, rho)
    rho *= dx
    beta_tmp *= 2.0

# write density matrix to file
Z = sum(rho[j, j] for j in range(nx + 1)) * dx
pi_of_x = [rho[j, j] / Z for j in range(nx + 1)]
f = open('data_harm_matrixsquaring_beta' + str(beta) + '.dat', 'w')
for j in range(nx + 1):
    f.write(str(x[j]) + ' ' + str(rho[j, j] / Z) + '\n')
f.close()

# plot probability distribution (approx and exact)
pylab.plot(x, pi_of_x, c='blue', linewidth=2.0, label='an-harmonic')

# Plot exact Quantum Probability Distribution
y_quant = [(prob_quant(a, beta)) for a in x]  
pylab.plot(x, y_quant, 'g', c='red', linewidth=2.0, label='harmonic')

pylab.title('Harmonic and An-harmonic Density Matrix\
             \nDistributions for Beta = ' +str(beta), fontsize = 18)
pylab.xlabel('$x$', fontsize = 20)
pylab.ylabel('$\pi(x)$', fontsize = 20)
pylab.xlim(-2.0, 2.0)
pylab.legend(loc='best')
pylab.savefig('C1_plot_anharmonic_oscillator_Beta=%d.png' % beta) # % beta)
pylab.show()

