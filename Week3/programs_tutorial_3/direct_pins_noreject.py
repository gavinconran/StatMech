import random

N = 10
L = 20.0
sigma = 0.75
n_runs = 800
for run in range(n_runs):
    # random selct poistions on the deflated line
    y = [random.uniform(0.0, L - 2 * N * sigma) for k in range(N)]
    # sort works for 1-D but maked algorithm redundant for more than 1-D
    y.sort()
    # Take care of inflation
    print [y[i] + (2 * i + 1) * sigma for i in range(N)]
