import random

L = 9 #4
b = -0.5 #0 #0.1
x = 0
nsteps = 10000000 #1000
l = []
for step in range(nsteps):
    if random.uniform(0.0, 1.0) < 0.5 + b:
        dx = 1
    else:
        dx = -1
    if x + dx >= 0 and x + dx < L:
        x += dx
    l.append(x)

print sum([1 for x in l if x == 0])
print sum([1 for x in l if x == 1])
print sum([1 for x in l if x == 2])
print sum([1 for x in l if x == 3])
print sum([1 for x in l if x == 4])
print sum([1 for x in l if x == 5])
print sum([1 for x in l if x == 6])
print sum([1 for x in l if x == 7])
