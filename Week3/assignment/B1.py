##B1.py

# Replicating Alder & Wainwright's first phase transition in a continuous 2-D system 
# using a numerical simulation based on Markov-chain Monte Carlo simulations

import random, math

# function to test periodic boundary conditions
def dist(x,y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return  math.sqrt(d_x**2 + d_y**2)

# function moves disk within periodic boundary conditions
def move_disk(disk):
    moved_disk = []
    moved_x = disk[0] % 1.0
    moved_y = disk[1] % 1.0
    moved_disk.append(moved_x)
    moved_disk.append(moved_y)
    return moved_disk

L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
sigma = 0.15
sigma_sq = sigma ** 2
delta = 0.1
n_steps = 100
for steps in range(n_steps):
    # key element: random choice of one disk whose coorditaes we alter slightly
    a = random.choice(L)
    b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
    # Compute the min. distance between all points (includes boundary conditions
    min_dist = min(dist(b, c) for c in L if c != a)
    # if min_dist is greater than 2 times the radius of two disks accept the move
    if (min_dist > 2.0 * sigma):
        a[:] = b
        # x and y positions of each disk are folded back into the interval 0.0 <= x < 1.0
        for disk in L:
            disk = move_disk(disk)


print L
