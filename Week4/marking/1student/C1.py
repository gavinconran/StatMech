import random

d_highest = 200
delta = 0.1
n_trials = 10000000

# store values for q and v_sph
# let's make the indexing intuitive
v_sph = 2

for d in range(1, d_highest):
    # Calculates Q(d+1)
    X = [0.0]*d
    n_hits = 0
    old_radius_square = 0.0
   
    for i in range(n_trials):
        k = random.randint(0, d - 1)
        alpha = random.uniform(-1.0, 1.0)
        x_old_k = X[k]
        x_new_k = x_old_k + random.uniform(-delta, delta)
        new_radius_square = old_radius_square + x_new_k**2 - x_old_k**2
        if new_radius_square < 1.0:
            X[k] = x_new_k
            old_radius_square = new_radius_square
        if old_radius_square + alpha**2 < 1.0:
            n_hits += 1
    q = 2.0 * n_hits / float(n_trials)  # <Q(d+1)>
    v_sph *= q # V_sph(d+1)
    print "<Q_%d>: %f, v_sph_%d: %g" % (d+1, q, d+1, v_sph)

