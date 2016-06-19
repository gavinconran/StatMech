import random, math, pylab

# This will calculate Q(d+1)
d = 3
n_trials = 10000000
delta = 0.1
old_radius_square = 0
x = [0] * d
n_hit = 0
r = []

for i in range(n_trials):
    k = random.randint(0, d - 1)
    x_old_k = x[k]
    x_new_k = x_old_k + random.uniform(-delta, delta)
    new_radius_square = old_radius_square + (x_new_k ** 2) - (x_old_k ** 2)
    # Check to see if new position is inside the sphere.  If so, accept the move, otherwise stay where we are.
    if math.sqrt(new_radius_square) < 1.:
        x[k] = x_new_k
        old_radius_square = new_radius_square
    z = random.uniform(-1,1)
    if math.sqrt(old_radius_square + z**2) < 1.:
        n_hit += 1
        r.append(math.sqrt(old_radius_square + z**2)) 
print n_hit, n_trials, 2.*float(n_hit)/n_trials

pylab.hist(r,50,normed=True)
x_plot = [a / 100.0 for a in xrange(1, 101)]
y_plot = [(4. * math.pow(a,3)) for a in x_plot]
#y_plot = [(20. * math.pow(a,19)) for a in x_plot]
pylab.plot(x_plot, y_plot, linewidth=1.5, color='r')
pylab.show()
