# B1.py
# Markov-chain program, generalization of markov_pi.py, that samples reasonably well in any dimension d
# works for general d
import random, math, pylab
import numpy as np

# no of dimensions
d=20

x = [0.0] * d
delta = 0.1
n_trials = 400000
n_hits = 0
old_radius_square = 0.0
data = []
data.append(old_radius_square)

# simulation starting point
for i in range(n_trials):
    # Instead of modifying all components of x at a time, as we did in markov_pi.py, 
    # modify only one component at each iteration i
    k = random.randint(0, d - 1)
    x_old_k = x[k]
    x_new_k = x_old_k + random.uniform(-delta, delta)
    
    new_radius_square = old_radius_square + x_new_k ** 2 - x_old_k ** 2
    # check to see if the pebble will still be in the sphere after next throw
    if (0.0 <= new_radius_square and new_radius_square <= 1.0):
        x[k] = x_new_k  # set x[k] to new value of x_new_k
        old_radius_square = new_radius_square # update old_radius_square
        
    alpha = random.uniform(-1.0, 1.0)     
    if (new_radius_square + alpha**2 < 1.0): 
        n_hits += 1
        data.append(math.sqrt(old_radius_square))

# print <Q_4>, the average value
# this is the ratio of the sphere volume for d=4 to the sphere volume for d=3  
Q4 = 2 * n_hits / float(n_trials)   
print Q4


pylab.hist(data, 100, normed=True)
x = np.arange(0.0, 1.0, 0.01)
power = d-1
y = [4 * 4 * r**power for r in x]
pylab.plot(x, y, c='red', linewidth=2.0)
pylab.title('$Norm(r)$ $versus$ $r$', fontsize = 25)
pylab.xlabel('$r$', fontsize = 20)
pylab.ylabel('$Norm(r)$', fontsize = 20)
pylab.savefig('B1_d=20.png')
pylab.show()



