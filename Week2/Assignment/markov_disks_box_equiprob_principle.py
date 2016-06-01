import random

# function returns a new Markov-chain configuration 
def markov_disks_box(N, sigma, delta, L):    
    sigma_sq = sigma ** 2
    count = 0
    for k in range(N):
        # key element: random choice of one disk whose coorditaes we alter slightly
        a = random.choice(L)
        b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
        min_dist = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in L if c != a)
        box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > 1.0 - sigma
        if not (box_cond or min_dist < 4.0 * sigma ** 2):
            a[:] = b
        else:
            count += 1
    return L, count


sigma = 0.15
delta = 0.1
n_runs = 1000000
del_xy = 0.05

conf_a = ((0.30, 0.30), (0.30, 0.70), (0.70, 0.30), (0.70,0.70))
conf_b = ((0.20, 0.20), (0.20, 0.80), (0.75, 0.25), (0.75,0.75))
conf_c = ((0.30, 0.20), (0.30, 0.80), (0.70, 0.20), (0.70,0.70))
configurations = [conf_a, conf_b, conf_c]
hits = {conf_a: 0, conf_b: 0, conf_c: 0}
x_vec = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
pebble_count = 0
for run in range(n_runs):
    x_vec, count = markov_disks_box(4, sigma, delta, x_vec)
    pebble_count += count
    for conf in configurations:
        condition_hit = True
        for b in conf:
            condition_b = min(max(abs(a[0] - b[0]), abs(a[1] - b[1])) for a in x_vec) < del_xy
            condition_hit *= condition_b
        if condition_hit:
            hits[conf] += 1

for conf in configurations:
    print conf, hits[conf] 

#print markov_disks_box(n_steps, sigma, delta)
