import random, math
from datetime import datetime
random.seed(datetime.now())

def square(list):
    return [i ** 2 for i in list]

def V_sph(dim):
    return math.pi ** (dim / 2.0) / math.gamma(dim / 2.0 + 1.0)

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

#Q = []
#V = []
#V.append(2.)
#n_trials = 10000000
#for d in range(1,20):
#    Q.append(find_Q(n_trials,d))
#    V.append(V[d-1] * Q[d-1][1])
#    print d+1, Q[d-1][1], V[d]
    
trials = [1, 10, 100, 1000, 10000, 100000, 1000000]
n_runs = 10

for n_trials in trials:
    V_running = []
    for runs in range(n_runs):
        V = []
        Q = []
        V.append(2.)
        for d in range(1,21):
            Q.append(find_Q(n_trials,d))
            V.append(V[d-1] * Q[d-1][1])
            #print d+1, Q[d-1][1], V[d]
        V_running.append(V[19])
    #print len(V_running), V_running, square(V_running)
    #print n_runs, sum(V_running), sum(square(V_running))
    alpha = sum(V_running)/n_runs
    beta = sum(square(V_running))/n_runs
    #print alpha**2, beta
    error_estimate = (math.sqrt(beta - alpha**2))/ math.sqrt(n_runs)
    print n_trials, alpha, V_sph(20), error_estimate, V_sph(20) - alpha, (V_sph(20) - alpha) / error_estimate
