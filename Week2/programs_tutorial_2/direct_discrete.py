# 1 dimensional simulation with conditions
# creates an equiprobable distribution of configurations 

import random
from sets import Set

configurations = {(0, 3): 'a', (0, 4): 'b', (1, 4): 'c',
                  (3, 0): 'd', (4, 0): 'e', (4, 1): 'f'}
counts = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0}

confSet = Set() # used to store unique configurations

n_runs = 100000
for run in range(n_runs):
    while True:
        red_rod = random.randint(0, 4)
        blue_rod = random.randint(0, 4)
        if abs(red_rod - blue_rod) > 2: break
    conf = configurations[(red_rod, blue_rod)]
    confSet.add(conf)    # adds configuration to set
    counts[conf] += 1
for conf in counts:
    print conf, counts[conf] / float(n_runs)

# prints out number of unique configurations
print "No. of configurations"
print len(confSet)
