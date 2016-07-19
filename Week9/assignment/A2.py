# A2.py

import math, random
from prettytable import PrettyTable

def V(x, y):
    pot  = -4.0 * x ** 2 - x ** 3 + 4.0 * x ** 4
    pot += -4.0 * y ** 2 - y ** 3 + 4.0 * y ** 4
    return pot


gamma = 0.4
gammas = [0.0025, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
success_rate = []

for gamma in gammas:
    n_runs = 100
    n_success = 0
    xmin, ymin = 0.807044513157, 0.807044513157
    for run in range(n_runs):
        T = 4.0
        x, y = 0.0, 0.0
        delta = 0.1
        step = 0
        acc = 0
        while T > 0.00001:
            step += 1
            if step == 100:
                T *= (1.0 - gamma)
                if acc < 30:
                   delta /= 1.2
                elif acc > 70:
                   delta *= 1.2
                step = 0
                acc = 0
            xnew = x + random.uniform(-delta, delta)
            ynew = y + random.uniform(-delta, delta)
            if abs(xnew) < 1.0 and abs(ynew) < 1.0 and \
                    random.uniform(0.0, 1.0) < math.exp(- (V(xnew, ynew) - V(x, y)) / T):
                x = xnew
                y = ynew
                acc += 1
        if math.sqrt((x - xmin) ** 2 + (y - ymin) ** 2) < 0.1:
            n_success += 1
    #print gamma, '\t', n_success / float(n_runs)
    success_rate.append(n_success / float(n_runs))

#print out results
t = PrettyTable(['Gamma', 'Success Rate'])
for i in range(len(gammas)):
    t.add_row([gammas[i], success_rate[i]])
print t
