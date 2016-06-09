import random, math
import pylab
import os, random


def show_conf(L, sigma, title, fname):
    pylab.axes()
    for [x, y] in L:
        for ix in range(-1, 2):
            for iy in range(-1, 2):
                cir = pylab.Circle((x + ix, y + iy), radius=sigma,  fc='r')
                pylab.gca().add_patch(cir)
    pylab.axis('scaled')
    pylab.title(title)
    pylab.axis([0.0, 1.0, 0.0, 1.0])
    pylab.savefig(fname)
    pylab.show()
    pylab.close()


def dist(x,y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return  math.sqrt(d_x**2 + d_y**2)
    
N = 256
k = int(math.sqrt(N))
eta = 0.72
sigma = math.sqrt(eta/(math.pi*N))
filename = 'disk_configuration_N%i_eta%.2f.txt' % (N, eta)
if os.path.isfile(filename):
    f = open(filename, 'r')
    L = []
    for line in f:
        a, b = line.split()
        L.append([float(a), float(b)])
    f.close()
    print 'starting from file', filename
else:
    delxy = 1.0 / (2*k) 
    two_delxy = 2 * delxy
    L = [[delxy + i * two_delxy, delxy + j * two_delxy] for i in range(k) for j in range(k)]
    print 'starting from a square-lattice initial configuration'
delta = 0.5 * sigma
n_steps = 000
for steps in range(n_steps):
    a = random.choice(L)
    b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
    for i in range(2):
	b[i] = b[i] % 1.0
    min_dist = min(dist(b, c) for c in L if c != a)
    if min_dist >= 2 * sigma:
        a[:] = b

f = open(filename, 'w')
for a in L[:]:
   f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
f.close()
show_conf(L, sigma, 'markov-chain-sampling: N=%i, eta=%.2f' % (N, eta), 'last_configuration_N%d_eta%.2f.png' %(N, eta))
