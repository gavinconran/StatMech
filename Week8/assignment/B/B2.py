# B2.py
# extension of B1_2.py and A2.py
# Wolff cluster Monte Carlo algorithm for the Ising model

import random, math, os

def energy(S, N, nbr):
    E = 0.0
    for k in range(N):
        E -=  S[k] * sum(S[nn] for nn in nbr[k])
    return 0.5 * E

L_List = [2, 4, 8, 16, 32]

T = 2.27 #2.0
p  = 1.0 - math.exp(-2.0 / T)
nsteps = 10000 #1000
print "nsteps: ", nsteps

for L in L_List:
    N = L * L

    nbr = {i : ((i // L) * L + (i + 1) % L, (i + L) % N,
            (i // L) * L + (i - 1) % L, (i - L) % N)
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

    E = [energy(S, N, nbr)]
    for step in range(nsteps):
        k = random.randint(0, N - 1)
        Pocket, Cluster = [k], [k]
        while Pocket != []:
            #j = random.choice(Pocket)
            j = Pocket.pop()
            for l in nbr[j]:
                if S[l] == S[j] and l not in Cluster \
                       and random.uniform(0.0, 1.0) < p:
                    Pocket.append(l)
                    Cluster.append(l)
            #Pocket.remove(j)
        for jj in Cluster:
            S[jj] *= -1
        E.append(energy(S, N, nbr))

    # compute specific heat capacity
    E_mean = sum(E) / len(E)
    E2_mean = sum(a ** 2 for a in E) / len(E)
    cv = (E2_mean - E_mean ** 2 ) / N / T ** 2
    print 'L: ', L, 'specific heat capacity:', cv

    # write out the final configuration on a file,
    f = open(filename, 'w')
    for a in S:
       f.write(str(a) + '\n')
    f.close()

