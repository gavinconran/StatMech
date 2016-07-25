import random
from sets import Set

L = 7 #3
t_max = 1000
site = [0, 0]
sitet = (0, 0)
configs = Set()
for t in range(t_max):
    delta = random.choice([[1, 0], [0, 1], [-1, 0], [0, -1]])
    site[0] = (site[0] + delta[0]) % L
    site[1] = (site[1] + delta[1]) % L
    newt = (site[0], site[1])
    configs.add(newt)
print site
print len(configs)
