# Bose-Einstein condensation.
# At a well defined temperature, Bosons clump together in the center of the trap: this is Bose-Einstein condensation.
# It was first achieved, in experimental harmonic traps just like ours , in 1995, by Cornell and Wieman, and also by Ketterle,
# Note: no particle indices
# positions x, y and z are the keys of a dictionary called positions, the positions for when tau=0
# the values of the dictionary are the values of the positions when tau=beta, the positions of the permutation partners
# Output: you see configurations x, y and z of about 1000 ideal bosons in an harmonic trap at termperature T.



import random, math, pylab, mpl_toolkits.mplot3d

# used at multiples of the inverse temperature beta, corresponding to the length of the permutation cycle.
# We use it to resample the positions of the entire cycle. 
def levy_harmonic_path(k, beta):
    xk = tuple([random.gauss(0.0, 1.0 / math.sqrt(2.0 *
                math.tanh(k * beta / 2.0))) for d in range(3)])
    x = [xk]
    for j in range(1, k):
        Upsilon_1 = (1.0 / math.tanh(beta) +
                     1.0 / math.tanh((k - j) * beta))
        Upsilon_2 = [x[j - 1][d] / math.sinh(beta) + xk[d] /
                     math.sinh((k - j) * beta) for d in range(3)]
        x_mean = [Upsilon_2[d] / Upsilon_1 for d in range(3)]
        sigma = 1.0 / math.sqrt(Upsilon_1)
        dummy = [random.gauss(x_mean[d], sigma) for d in range(3)]
        x.append(tuple(dummy))
    return x

# computes the off-diagonal harmonic density matrix.
# We use it to organize the exchange of two elements. 
def rho_harm(x, xp, beta):
    Upsilon_1 = sum((x[d] + xp[d]) ** 2 / 4.0 *
                    math.tanh(beta / 2.0) for d in range(3))
    Upsilon_2 = sum((x[d] - xp[d]) ** 2 / 4.0 /
                    math.tanh(beta / 2.0) for d in range(3))
    return math.exp(- Upsilon_1 - Upsilon_2)

N = 256
T_star = 0.6
beta = 1.0 / (T_star * N ** (1.0 / 3.0))
nsteps = 1000000
positions = {}
# initialise positions using levy_harmonic_path as in homework6 / C2.py
for j in range(N):
    a = levy_harmonic_path(1, beta)
    positions[a[0]] = a[0]
# for each particle move:
for step in range(nsteps):
    # sample random particle
    boson_a = random.choice(positions.keys())
    perm_cycle = []
    # identify permuttaion cycle 
    while True:
        perm_cycle.append(boson_a)
        boson_b = positions.pop(boson_a)
        if boson_b == perm_cycle[0]: break
        else: boson_a = boson_b
    k = len(perm_cycle)
    # sample the new Levy quantum path for entire cycle from levy quantum path
    perm_cycle = levy_harmonic_path(k, beta)
    positions[perm_cycle[-1]] = perm_cycle[0]
    for j in range(len(perm_cycle) - 1):
        positions[perm_cycle[j]] = perm_cycle[j + 1]
    # for each permutation move, sample two random particles
    # atempt an exchange of their permutation partners
    a_1 = random.choice(positions.keys())
    b_1 = positions.pop(a_1)
    a_2 = random.choice(positions.keys())
    b_2 = positions.pop(a_2)
    weight_new = rho_harm(a_1, b_2, beta) * rho_harm(a_2, b_1, beta)
    weight_old = rho_harm(a_1, b_1, beta) * rho_harm(a_2, b_2, beta)
    if random.uniform(0.0, 1.0) < weight_new / weight_old:
        positions[a_1] = b_2
        positions[a_2] = b_1
    else:
        positions[a_1] = b_1
        positions[a_2] = b_2


# create graphic
fig = pylab.figure()
ax = mpl_toolkits.mplot3d.axes3d.Axes3D(fig)
ax.set_aspect('equal')
list_colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
n_colors = len(list_colors)
dict_colors = {}
i_color = 0
# find and plot permutation cycles:
while positions:
    x, y, z = [], [], []
    starting_boson = positions.keys()[0]
    boson_old = starting_boson
    while True:
        x.append(boson_old[0])
        y.append(boson_old[1])
        z.append(boson_old[2])
        boson_new = positions.pop(boson_old)
        if boson_new == starting_boson: break
        else: boson_old = boson_new
    len_cycle = len(x)
    if len_cycle > 2:
        x.append(x[0])
        y.append(y[0])
        z.append(z[0])
    if len_cycle in dict_colors:
        color = dict_colors[len_cycle]
        ax.plot(x, y, z, color + '+-', lw=0.75)
    else:
        color = list_colors[i_color]
        i_color = (i_color + 1) % n_colors
        dict_colors[len_cycle] = color
        ax.plot(x, y, z, color + '+-', label='k=%i' % len_cycle, lw=0.75)
# finalize plot
pylab.title('$N=%i$, $T^*=%s$' % (N, T_star))
pylab.legend()
ax.set_xlabel('$x$', fontsize=16)
ax.set_ylabel('$y$', fontsize=16)
ax.set_zlabel('$z$', fontsize=16)
ax.set_xlim3d([-8, 8])
ax.set_ylim3d([-8, 8])
ax.set_zlim3d([-8, 8])
pylab.savefig('snapshot_bosons_3d_N%04i_Tstar%04.2f.png' % (N, T_star))
pylab.show()
