import random, math

def V_sph(dim):
    return math.pi ** (dim / 2.0) / math.gamma(dim / 2.0 + 1.0)

d_highest = 20
delta = 0.1
n_runs = 10
n_runs_sqrt = math.sqrt(n_runs)
exact = V_sph(d_highest)

print "n_trials | <V_sph(20)> | V_sph(20) (exact) | error       | difference"

for n_trials in [10**n for n in range(1,7)]:
    v_sph_sum = 0.0
    v_sph_sq_sum = 0.0
    for run in range(0, n_runs):
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
        #print "<Q_%d>: %f, v_sph_%d: %g" % (d_highest, q, d_highest, v_sph)
        v_sph_sum += v_sph
        v_sph_sq_sum += v_sph**2
    v_sph_avg = v_sph_sum / float(n_runs)       # <V_sph(20)>
    v_sph_sq_avg = v_sph_sq_sum / float(n_runs) # <V_sph(20)^2>
    err = math.sqrt(v_sph_sq_avg - v_sph_avg**2) / n_runs_sqrt
    diff = v_sph_avg - exact
    print "%8d | %11g | %17g | %11g | %11g" % (n_trials, v_sph_avg, exact, err, diff)
