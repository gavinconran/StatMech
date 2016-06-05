# generates random configurations of N clothes-pins using the tabula rasa rule.

import random

N = 15
L = 10.0
sigma = 0.1
n_configs = 100
tabula = 0
for config in range(n_configs):
    x = []
    while len(x) < N:
        x.append(random.uniform(sigma, L - sigma))
        for k in range(len(x) - 1):
            if abs(x[-1] - x[k]) < 2.0 * sigma:
                x = []
                tabula += 1
                break
    print x

print tabula / float(n_configs)
