import random, math

d = 3
X = [0.0]*d
delta = 0.1
n_trials = 400000
n_hits = 0
for i in range(n_trials):
    del_x = [random.uniform(-delta, delta) for dim in range(d)]
    alpha = random.uniform(-1.0, 1.0)
    if math.fsum([(X[i]+del_x[i])**2 for i in range(d)]) < 1.0:
        X = [sum(x) for x in zip(X, del_x)]
    if math.fsum([X[i]**2 for i in range(d)]) + alpha**2 < 1.0:
        n_hits += 1
print 2.0 * n_hits / float(n_trials)

