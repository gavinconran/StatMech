# Assignment 4: A2.py
# Modified from markov_pi.py
# samples points within a disk rather than inside the square


import random, math

# simulation starting point
x, y = 0.0, 0.0
delta = 0.1
n_trials = 4000
n_hits = 0
for i in range(n_trials):
    del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
    # additioanl line
    # What is the point of z?
    z = random.uniform(-1.0, 1.0) 
    # check to see if the pebble will still be in the disk after next throw
    #if (math.sqrt((x + del_x)**2 + (y+del_y)**2) < 1.0):
    if ((x + del_x)**2 + (y+del_y)**2 < 1.0):
        x, y = x + del_x, y + del_y
        
    if x**2 + y**2 + z**2 < 1.0: 
        n_hits += 1

# print <Q_3>, the average value
# this is the ratio of the sphere volume for d=3 to the sphere volume for d=2        
print 2 * n_hits / float(n_trials)


