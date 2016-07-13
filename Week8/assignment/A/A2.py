# A2.py
# A1.p plus new features
# Comapres "mean energy per spin" obtained from Local metroplis algorithm and known result

import random, math, os, pylab

def energy(S, N, nbr):
    E = 0.0
    for k in range(N):
        E -=  S[k] * sum(S[nn] for nn in nbr[k])
    return 0.5 * E

L = 128 #32
N = L * L
T = 1.0 #2.27 #3.0
nsteps = N * 1000
print 'L: ', L, " ,T = ", T, " ,nsteps = ", nsteps

nbr = {i : ((i // L) * L + (i + 1) % L, (i + L) % N,
        (i // L) * L + (i - 1) % L, (i - L) % N) \
                                for i in range(N)}

# read in the initial configuration from a file (if possible)
filename = 'data_local_'+ str(L) + '_' + str(T) + '.txt'
if os.path.isfile(filename):
    f = open(filename, 'r')
    S = []
    for line in f:
        S.append(int(line))
    f.close()
    print 'Starting from file', filename
else:
    S = [random.choice([1, -1]) for k in range(N)]
    print 'Starting from a random configuration'

beta = 1.0 / T
Energy = energy(S, N, nbr)
E = []
for step in xrange(nsteps):
    k = random.randint(0, N - 1)
    delta_E = 2.0 * S[k] * sum(S[nn] for nn in nbr[k])
    if random.uniform(0.0, 1.0) < math.exp(-beta * delta_E):
        S[k] *= -1
        Energy += delta_E
    E.append(Energy)
print 'mean energy per spin:', sum(E) / float(len(E) * N)

# write out the final configuration on a file,
f = open(filename, 'w')
for a in S:
   f.write(str(a) + '\n')
f.close()

# show a plot of the final configuration
def x_y(k, L):
    y = k // L
    x = k - y * L
    return x, y

conf = [[0 for x in range(L)] for y in range(L)]
for k in range(N):
    x, y = x_y(k, L)
    conf[x][y] = S[k]

pylab.imshow(conf, extent=[0, L, 0, L], interpolation='nearest')
pylab.set_cmap('hot')
pylab.title('Local_'+ str(T) + '_' + str(L))
pylab.savefig('plot_A2_local_'+ str(T) + '_' + str(L)+ '.png')
pylab.show()
