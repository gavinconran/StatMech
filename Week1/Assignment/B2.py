import random

x, y = 1.0, 1.0
n_trials = 2**12

for delta in [0.062, 0.125, 0.25, 0.5, 1.0, 2.0, 4.0]:
    acceptance = 0 # used to count the number of accepted moves
    n_hits = 0
    for run in range(n_trials):
        del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
        if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
            x, y = x + del_x, y + del_y
            acceptance += 1
    print delta, acceptance / float(n_trials)

