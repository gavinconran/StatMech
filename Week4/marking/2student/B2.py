import random, math

def find_Q(n_trials,d):
    delta = 0.1
    old_radius_square = 0
    x = [0] * d
    n_hit = 0   
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
    return n_hit, 2.*float(n_hit)/n_trials

def V_sph(dim):
    return math.pi ** (dim / 2.0) / math.gamma(dim / 2.0 + 1.0)

n_trials = 10000000
print V_sph(4)/V_sph(3), find_Q(n_trials,3)[1]
print V_sph(200)/V_sph(199), find_Q(n_trials,199)[1]
