# C2.py
# Compute Density matrix for anharmonic potential using Monte Carlo Path Integrals

import math, random, pylab

# returns anharmonic potential
def V(x, cubic, quartic):
    return x ** 2 / 2.0 + cubic * x ** 3 + quartic * x ** 4

# returns rho_free off-diagonal density matrix
def rho_free(x, y, beta):    
    return math.exp(-(x - y) ** 2 / (2.0 * beta)) 

def read_file(filename):
    list_x = []
    list_y = []
    with open(filename) as f:
        for line in f:
            x, y = line.split()
            list_x.append(float(x))
            list_y.append(float(y))
    f.close()
    return list_x, list_y


beta = 4.0
N = 16                                             # number of slices
dtau = beta / N                                   # time slice 
delta = 1.0                                       # maximum displacement on one slice
n_steps = 10000000                               # number of Monte Carlo steps
x = [0.0] * N                                     # initial path
data = []
cubic = -1.0
quartic = 1.0 # 0
for step in range(n_steps):
    k = random.randint(0, N - 1)                  # random slice
    knext, kprev = (k + 1) % N, (k - 1) % N       # next/previous slices
    x_new = x[k] + random.uniform(-delta, delta)  # new position at slice k
    old_weight  = (rho_free(x[knext], x[k], dtau) *
                   rho_free(x[k], x[kprev], dtau) *
                   math.exp(-dtau * V(x[k], cubic, quartic)))
    new_weight  = (rho_free(x[knext], x_new, dtau) *
                   rho_free(x_new, x[kprev], dtau) *
                   math.exp(-dtau * V(x_new, cubic, quartic)))
    if random.uniform(0.0, 1.0) < new_weight / old_weight:
        x[k] = x_new

    if step % 10 == 0:
        data.append(x[0])
        #for i in range(N):
        #    data.append(x[i])
    
## Create Graphic
pylab.figure()
# Histogram of formed from path-Integral Monte Carlo
pylab.hist(data, 100, normed = 'True', label='Quantum MC')

# PDF of formed from matrix-multiplication (convolution)
filename="data_harm_matrixsquaring_beta4.0.dat"
list_x, list_y = read_file(filename)
pylab.plot(list_x, list_y, c='red', linewidth=2.0, label='Matrix Mult')

pylab.title('Harmonic and An-harmonic Density Matrix\
             \nDistributions for Beta = ' +str(beta), fontsize = 18)

pylab.title('Quantum Monte Carlo and Matrix Multiplication\
            \nNormalized Histogram for cubic = '+str(cubic)+' and Quartic = '+str(quartic)+ ' for\
            \nBeta = ' +str(beta), fontsize = 18)
pylab.xlabel('$x$', fontsize = 20)
pylab.ylabel('$\pi(x)$', fontsize = 20)
pylab.xlim(-2.0, 3.0)
pylab.legend(loc='best')
pylab.savefig('x0_%d_plot_Path_integral_MC_B=%d_N=%d.png' % (n_steps, beta, N))
pylab.show()
