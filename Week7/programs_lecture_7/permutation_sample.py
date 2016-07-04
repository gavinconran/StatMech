# permutations of n elements in a list.
# At each step, we may exchange two random elements.
# This random transposition algorithm is a Markov-Chain algorithm


import random

N = 3
statistics = {}
L = range(N)
nsteps = 10000
for step in range(nsteps):
    # two random indices i, j
    i = random.randint(0, N - 1)
    j = random.randint(0, N - 1)
    # exchange positions
    L[i], L[j] = L[j], L[i]
    # Rejection / acceptance according to Metropolice algo
    if tuple(L) in statistics: 
        statistics[tuple(L)] += 1
    else:
        statistics[tuple(L)] = 1
    print L
    print range(N)
    print

for item in statistics:
    print item, statistics[item]
