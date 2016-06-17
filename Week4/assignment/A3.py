# Assignment 4: A3.py
# Modified from A2.py
# computes the Volume of  aunit sphere in 4-D


import random, math

# simulation starting point
x, y, z = 0.0, 0.0, 0.0
delta = 0.1
n_trials = 40000000
n_hits = 0
for i in range(n_trials):
    del_x, del_y, del_z = random.uniform(-delta, delta), random.uniform(-delta, delta), random.uniform(-delta, delta)
    # additioanl line
    # What is the point of z?
    alpha = random.uniform(-1.0, 1.0) 
    # check to see if the pebble will still be in the disk after next throw
    if (math.sqrt((x + del_x)**2 + (y+del_y)**2 + (z+del_z)**2) < 1.0):
        x, y, z = x + del_x, y + del_y, z + del_z
        
    if x**2 + y**2 + z**2 + alpha**2 < 1.0: 
        n_hits += 1

# print <Q_4>, the average value
# this is the ratio of the sphere volume for d=4 to the sphere volume for d=3  
Q4 = 2 * n_hits / float(n_trials)   

### Check that the volume V_sph(d=4) of the four-dimensional unit sphere can be given by three equivalent formulas:
#  Formula 1: V_sph(d=4) = pi^2 / 2
print "V_sphere(d=4) = ", math.pi**2/float(2) 

#Formula 2: V_sph(d=4) = V_sph(3) * Q_4, approximately equal to: V_sph(3) * <Q_4>
Q3 = 1.33302025  # calculated by A2.py
V_sph_d3 = Q3 * math.pi
print "V_sphere(d=4) = ", V_sph_d3 * Q4

# Formula 3: V_sph(d=4) = V_sph(2) * Q_3 * Q_4, approximately equal to: V_sph(2) * <Q_3> * <Q_4>
V_sph_d2 = math.pi
print "V_sphere(d=4) ~ ", V_sph_d2 * Q3 * Q4 



