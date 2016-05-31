# 2 dimensional (box) simulation with conditions
# creates an equiprobable distribution of configurations 
# Discards overlap configurations as they are generated using distance measurement
# Output is the coords of all four disks in a non overlap configuration

import random, math

N = 4
sigma = 0.2
condition = False
while condition == False:
    L = [(random.uniform(sigma, 1.0 - sigma), random.uniform(sigma, 1.0 - sigma))]
    for k in range(1, N):
        a = (random.uniform(sigma, 1.0 - sigma), random.uniform(sigma, 1.0 - sigma))
        min_dist = min(math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) for b in L) 
        if min_dist < 2.0 * sigma: 
            condition = False
            break
        else:
            L.append(a)
            condition = True
print L
