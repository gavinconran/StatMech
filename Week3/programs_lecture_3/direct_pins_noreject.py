# direct sampling algorithm without rejections
# will be discussed in this week's tutorial
# which gives an analytical solution without rejections


import random

N = 15 #10  # Number of pegs
L = 1.0 #20.0  # Length of line
sigma = 0.75  # width of pin
n_runs = 800 # number of configurations
for run in range(n_runs):
    y = [random.uniform(0.0, L - 2 * N * sigma) for k in range(N)]
    y.sort()
    print [y[i] + (2 * i + 1) * sigma for i in range(N)]
