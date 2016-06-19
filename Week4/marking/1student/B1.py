import random, math
from matplotlib import pylab

d = 20 #4
X = [0.0]*d
delta = 0.1
n_trials = 400000
hist_data = []
#n_hits = 0
old_radius_square = 0.0
for i in range(n_trials):
    k = random.randint(0, d - 1)
    #alpha = random.uniform(-1.0, 1.0)
    x_old_k = X[k]
    x_new_k = x_old_k + random.uniform(-delta, delta)
    new_radius_square = old_radius_square + x_new_k**2 - x_old_k**2
    if new_radius_square < 1.0:
        X[k] = x_new_k
        old_radius_square = new_radius_square
#        if new_radius_square + alpha**2 < 1.0:
#            n_hits += 1
#    elif old_radius_square + alpha**2 < 1.0:
#        n_hits += 1
    hist_data.append(math.sqrt(old_radius_square))
#print 2.0 * n_hits / float(n_trials)
pylab.hist(hist_data, normed=True)
pylab.plot([x/100.0 for x in range(0,100)], [d*(y/100.0)**(d-1) for y in range(0,100)])
pylab.xlabel('Radius')
pylab.ylabel('Freq (Normalized)')
pylab.title('Radius histogram for d=' + str(d) + ', compared to ' + str(d) + 'r^' + str(d-1))
pylab.savefig("hist_" + str(d) + ".png")
