# Question 3

"""
# A12: markov-chain? maybe, this is the heat-bath algo for the ising Model which uses
# heat-bath acceptance rather than Metrpolis
import random, math

sigma = 0.16
L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
for t in range(100000):
    a = random.choice(L)
    while True:
        b = [random.uniform(sigma, 1.0 - sigma), random.uniform(sigma, 1.0 - sigma)]
        min_dist = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in L if c != a)
        if min_dist > 4.0 * sigma ** 2:
            a[:] = b
            break
    print L



# B12: markov-chain? Qui, for no periodic boundary conditions
import random, math

sigma = 0.16
L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
for t in range(100000):
    a = random.choice(L)
    b = [random.uniform(sigma, 1.0 - sigma), random.uniform(sigma, 1.0 - sigma)]
    min_dist = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in L if c != a)
    if min_dist > 4.0 * sigma ** 2:
        a[:] = b
    print L

"""
# C12: markov-chain? Non, we need the command a[:] = b rather than L.append(b)
import random, math

sigma = 0.16; delta = 0.1
L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
for t in range(10000):
    a = random.choice(L)
    L.remove(a)
    b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
    min_dist = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in L)
    box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > 1.0 - sigma # Non-Peroidic
    if not (box_cond or min_dist < 4.0 * sigma ** 2):
        L.append(b)
        print L
    else:
        L.append(a)


