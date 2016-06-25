# C3.py
# extension of C1.py
# computes density matrix for anharmonic oscillator
# Plots chart with approximate and exact probability distribution function (PDF)
# Compares Z and Z_pert

import math, numpy, pylab
from prettytable import PrettyTable

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

# return perturbative expression
def Energy_pert(n, cubic, quartic):
    return n + 0.5 - 15.0 / 4.0 * cubic **2 * (n ** 2 + n + 11.0 / 30.0) \
         + 3.0 / 2.0 * quartic * (n ** 2 + n + 1.0 / 2.0)

# returns the approximate partition function
def Z_pert(cubic, quartic, beta, n_max):
    Z = sum(math.exp(-beta * Energy_pert(n, cubic, quartic)) for n in range(n_max + 1))
    return Z


# Initialise variables
n_max = 20
x_max = 5 # 5 #50.0
nx = 100
dx = 2.0 * x_max / (nx - 1)
x = [i * dx for i in range(-(nx - 1) / 2, nx / 2 + 1)] 
beta_tmp = 2.0 ** (-8)                   # initial value of beta (power of 2)
beta     = 2.0 ** 1                          # actual value of beta (power of 2)
quarticList = [0.001, 0.01, 0.1, 0.2, 0.3, 0.4, 0.5]
cubicList = [-0.001, -0.01, -0.1, -0.2, -0.3, -0.4, -0.5]
ZResult = []
Z_pertResult = []
for quartic in quarticList:
    cubic = quartic * -1
    rho = rho_anharmonic_trotter(x, beta_tmp, cubic, quartic)  # density matrix at initial beta
    while beta_tmp < beta:
        rho = numpy.dot(rho, rho)
        rho *= dx
        beta_tmp *= 2.0

    # write density matrix to file
    Z = sum(rho[j, j] for j in range(nx + 1)) * dx
    ZResult.append(Z)
    Zpert = Z_pert(cubic, quartic, beta, n_max)
    Z_pertResult.append(Zpert)

#print out results
t = PrettyTable(['Cubic', 'Quartic', 'Matrix Mult Partition Fun (Z)' , 'Perturbation Partition Fun (Z_pert)'])
for i in range(len(quarticList)):
    t.add_row([cubicList[i], quarticList[i], ZResult[i], Z_pertResult[i]])
print t



