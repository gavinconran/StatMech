import random, math, pylab

x, y, z = 0.0, 0.0, 0.0
delta = 0.1
n_trials = 8000000
n_hits = 0

x_pos = []
y_pos = []
z_pos = []


for i in range(n_trials):
    del_x, del_y, del_z = random.uniform(-delta, delta), random.uniform(-delta, delta), random.uniform(-delta, delta)
    if math.sqrt((x + del_x)**2 + (y + del_y)**2 + (z + del_z)**2) < 1.0:
        x, y, z = x + del_x, y + del_y, z + del_z
        alpha = random.uniform(-1.0,1.0)
    if (x**2 + y**2 + z**2 + alpha**2) < 1.0: 
        n_hits += 1
        #x_pos.append(x)
        #y_pos.append(y)
        #z_pos.append(z)
ratio = (2. * n_hits)/float(n_trials)
print ratio

vol_4d_sphere = math.pow(math.pi,2)/2

Q_4 = (3. * math.pi) / 8.
ratio = (2. * n_hits)/float(n_trials)
#print vol_4d_sphere
print "N_trials: \t\t", n_trials
print "N_hits:\t\t\t", n_hits
print "Expected Q_4: \t\t", Q_4
print "Calculated Q_4: \t", ratio
print "Q4 ratio: \t\t", ratio / Q_4

est_Q4 = ratio
rule_2 = (4./3.) * math.pi * est_Q4
rule_3 = math.pi * est_Q3 * est_Q4
print "Rule 1 volume: \t\t", vol_4d_sphere
print "Rule 2 volume: \t\t", rule_2
print "Rule 3 volume: \t\t", rule_3
print "Rule 2 / Rule 1:\t", rule_2/vol_4d_sphere
print "Rule 3 / Rule 1:\t", rule_3/vol_4d_sphere
