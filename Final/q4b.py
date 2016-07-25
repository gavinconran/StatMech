import random

N = 8
nsteps = 1000000 #100
l = []
for step in range(nsteps):
    tmp = range(N)
    L = []
    while tmp != []:
        element = random.choice(tmp)
        tmp.remove(element)
        L.append(element)
    #print L[0]
    l.append(L[0])

print sum([1 for x in l if x == 0])
print sum([1 for x in l if x == 1])
print sum([1 for x in l if x == 2])
print sum([1 for x in l if x == 3])
print sum([1 for x in l if x == 4])
print sum([1 for x in l if x == 5])
print sum([1 for x in l if x == 6])
print sum([1 for x in l if x == 7])
