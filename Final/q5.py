import random

N = 52
nsteps = 1 #10000000 #100
L = range(N)
l = []
for step in range(nsteps):
    i = random.randint(0, N - 1)
    j = random.randint(0, N - 1)
    L[i], L[j] = L[j], L[i]
    print L[0]
    l.append(L[0])

"""
print sum([1 for x in l if x == 0])
print sum([1 for x in l if x == 1])
print sum([1 for x in l if x == 2])
print sum([1 for x in l if x == 3])
print sum([1 for x in l if x == 4])
print sum([1 for x in l if x == 5])
print sum([1 for x in l if x == 6])
print sum([1 for x in l if x == 7])
print sum([1 for x in l if x == 8])
print sum([1 for x in l if x == 9])
print sum([1 for x in l if x == 10])
print sum([1 for x in l if x == 11])
print sum([1 for x in l if x == 12])
print sum([1 for x in l if x == 13])
print sum([1 for x in l if x == 14])
print sum([1 for x in l if x == 15])
print sum([1 for x in l if x == 16])
print sum([1 for x in l if x == 17])
print sum([1 for x in l if x == 18])
print sum([1 for x in l if x == 19])
print sum([1 for x in l if x == 20])
print sum([1 for x in l if x == 21])
print sum([1 for x in l if x == 22])
print sum([1 for x in l if x == 23])
print sum([1 for x in l if x == 24])
print sum([1 for x in l if x == 25])
print sum([1 for x in l if x == 26])
print sum([1 for x in l if x == 27])
print sum([1 for x in l if x == 28])
print sum([1 for x in l if x == 29])
print sum([1 for x in l if x == 30])
print sum([1 for x in l if x == 31])
print sum([1 for x in l if x == 32])
print sum([1 for x in l if x == 33])
print sum([1 for x in l if x == 34])
print sum([1 for x in l if x == 35])
print sum([1 for x in l if x == 36])
print sum([1 for x in l if x == 37])
print sum([1 for x in l if x == 38])
print sum([1 for x in l if x == 39])
print sum([1 for x in l if x == 40])
print sum([1 for x in l if x == 41])
print sum([1 for x in l if x == 42])
print sum([1 for x in l if x == 43])
print sum([1 for x in l if x == 44])
print sum([1 for x in l if x == 45])
print sum([1 for x in l if x == 46])
print sum([1 for x in l if x == 47])
print sum([1 for x in l if x == 48])
print sum([1 for x in l if x == 49])
print sum([1 for x in l if x == 50])
print sum([1 for x in l if x == 51])
"""
analytic =  1 - 2 * (N - 1) / N ** 2
print analytic
