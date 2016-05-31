# 2 dimensional (box) simulation with conditions
# creates an equiprobable distribution of configurations 
# Discards overlap configurations at the end using Energy measurement (I think)
# Output is the coords of all four disks in a non overlap configuration


import random

N = 4
sigma = 0.2
pairs = [(i, j) for i in range(N - 1) for j in range(i + 1, N)]
while True:
    # Vector L: uniform random vector generated using a List comprehension
    L = [(random.uniform(sigma, 1.0 - sigma), random.uniform(sigma, 1.0 - sigma)) for k in range(N)]
    # Discrad from vector those configurations that overlap
    if  min((L[i][0] - L[j][0]) ** 2 + (L[i][1] - L[j][1]) ** 2 for i, j in pairs) > 4.0 * sigma ** 2: 
        break
print L
