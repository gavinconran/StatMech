import random
import numpy as np

N = 8
nsteps = 1000000
L = range(N)
l = []
for step in range(nsteps):
    i = random.randint(0, N - 1)
    j = random.randint(0, N - 1)
    L[i], L[j] = L[j], L[i]
    l.append(L[i])
    #print L[0]

print sum([1 for x in l if x == 0])
print sum([1 for x in l if x == 1])
print sum([1 for x in l if x == 2])
print sum([1 for x in l if x == 3])
print sum([1 for x in l if x == 4])
print sum([1 for x in l if x == 5])
print sum([1 for x in l if x == 6])
print sum([1 for x in l if x == 7])

