import random

def markov_disks_box(Ini, sigma):
    sigma = 0.15
    sigma_sq = sigma ** 2
    delta = 0.1
    a = random.choice(L)
    b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
    min_dist = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in Ini if c != a)
    box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > 1.0 - sigma
    if not (box_cond or min_dist < 4.0 * sigma_sq):
        a[:] = b
    return Ini

sigma = 0.15
del_xy = 0.05
n_runs = 10 ** 6
conf_a = ((0.30, 0.30), (0.30, 0.70), (0.70, 0.30), (0.70,0.70))
conf_b = ((0.20, 0.20), (0.20, 0.80), (0.75, 0.25), (0.75,0.75))
conf_c = ((0.30, 0.20), (0.30, 0.80), (0.70, 0.20), (0.70,0.70))
configurations = [conf_a, conf_b, conf_c]
hits = {conf_a: 0, conf_b: 0, conf_c: 0}

L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
for run in range(n_runs):
    xy_vec = markov_disks_box(L, sigma)
    for conf in configurations:
        condition_hit = True
        for b in conf:
            condition_b = min(max(abs(a[0] - b[0]), abs(a[1] - b[1])) for a in xy_vec) < del_xy
            condition_hit *= condition_b
            #print condition_hit
        if condition_hit:
            hits[conf] += 1
    L = xy_vec

for conf in configurations:
    print conf, hits[conf]
