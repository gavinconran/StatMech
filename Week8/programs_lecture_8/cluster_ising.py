# cluster_ising.py
# much faster than local monte carlo algo
# speed up increases with system size

import random, math

L = 100
N = L * L
nbr = {i : ((i // L) * L + (i + 1) % L, (i + L) % N,
            (i // L) * L + (i - 1) % L, (i - L) % N)
                                    for i in range(N)}
T = 2.5
p  = 1.0 - math.exp(-2.0 / T)
nsteps = 10000
S = [random.choice([1, -1]) for k in range(N)]
for step in range(nsteps):
    # take a random spin
    k = random.randint(0, N - 1)
    # place random spin into cluster and into the pocket
    Pocket, Cluster = [k], [k]
    while Pocket != []:
        # take a random element from the cluster
        j = random.choice(Pocket)
        # check all of the element's neighbours
        for l in nbr[j]:
            # for each of the enighbours check to see if NOT already in the cluster
            # whether it has the same sign AND
            # a random number between 0 and 1 is smaller than p 
            if S[l] == S[j] and l not in Cluster \
                   and random.uniform(0.0, 1.0) < p:
                # if all 3 conditions are satisfied
                # add the new spin to the cluster and the pocket
                Pocket.append(l)
                Cluster.append(l)
        # remove new spin from the pocket
        Pocket.remove(j)
    # once the pocket is empty
    # flip the entire cluster
    for j in Cluster:
        S[j] *= -1

print sum(S)
