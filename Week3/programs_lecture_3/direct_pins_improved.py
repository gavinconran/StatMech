# generates random configurations of N clothes-pins using the tabula rasa rule.
# but uses sorting trick

import random

# Good example of using sort to improve the running time of an algorithm
N = 5    # 15
L = 1.0  # 10.0
sigma = 0.075
n_configs = 100
tabula = 0
for config in range(n_configs):
    while True:
        x = [random.uniform(sigma, L - sigma) for k in range(N)]
        x.sort() # makes comparison much more efficient
        min_dist = min(x[k + 1] - x[k] for k in range(N - 1))
        if min_dist > 2.0 * sigma:
            print x
            break
        else:
            tabula += 1
            
print tabula / float(n_configs)
