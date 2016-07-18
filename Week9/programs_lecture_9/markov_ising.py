# markov_ising.py
# select a single spin and flip it
# accept with metropois acceptance probability
# Each spin flip involves an the order of N operations due ro computing lambda for each flip


import random, math

L = 32
N = L * L
nbr = {i : ((i // L) * L + (i + 1) % L, (i + L) % N,
            (i // L) * L + (i - 1) % L, (i - L) % N) \
                                    for i in range(N)}
nsteps = 1000000
T = 2.0
beta = 1.0 / T
S = [random.choice([1, -1]) for k in range(N)]
for step in range(nsteps):
    k = random.randint(0, N - 1)
    delta_E = 2.0 * S[k] * sum(S[nn] for nn in nbr[k])
    # metrolois acceptance/rejection
    if random.uniform(0.0, 1.0) < math.exp(-beta * delta_E):
        S[k] *= -1
print sum(S)

