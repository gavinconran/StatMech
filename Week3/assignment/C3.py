## C3.py
## B3.py plus:
## calculation of Psi_6 


# Replicating Alder & Wainwright's first phase transition in a continuous 2-D system 
# using a numerical simulation based on Markov-chain Monte Carlo simulations

import random, math, pylab, os, cmath

# function to compute distsnce beween 2 disks (with periodic boundary conditions)
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

# function prints out a configuration
def show_conf(L, sigma, title, fname):
    pylab.axes()
    for [x, y] in L:
        for ix in range(-1, 2):
            for iy in range(-1, 2):
                cir = pylab.Circle((x + ix, y + iy), radius=sigma,  fc='r')
                pylab.gca().add_patch(cir)
    pylab.axis('scaled')
    pylab.title(title)
    pylab.axis([0.0, 1.0, 0.0, 1.0])
    pylab.savefig(fname)
    pylab.show()
    pylab.close()


# function computes the distance vector, corrected for periodic boundary conditions. 
def delx_dely(x, y):
    d_x = (x[0] - y[0]) % 1.0
    if d_x > 0.5: d_x -= 1.0
    d_y = (x[1] - y[1]) % 1.0
    if d_y > 0.5: d_y -= 1.0
    return d_x, d_y

# Computed Psi_6, the Global Order Parameter
def Psi_6(L, sigma):
    sum_vector = 0j
    for i in range(N):
        vector  = 0j
        n_neighbor = 0
        for j in range(N):
            if dist(L[i], L[j]) < 2.8 * sigma and i != j:
                n_neighbor += 1
                dx, dy = delx_dely(L[j], L[i])
                angle = cmath.phase(complex(dx, dy))
                vector += cmath.exp(6.0j * angle)
        if n_neighbor > 0:
            vector /= n_neighbor
        sum_vector += vector
    return sum_vector / float(N)


# Set / deduce simulation parameters
N = 64 #10000 #1000000 #4 # number of disks
N_sqrt = int(math.sqrt(N))
eta = 0.72 #0.42 #0.72 #0.5 # covering density, eta
sigma = math.sqrt(eta / (N * math.pi)) # deduce sigma from eta
delta = 0.3 * sigma

## read initial conditions from an input file (if it exists)
filename = 'disk_configuration_N%i_eta%.2f.txt' % (N, eta)
if os.path.isfile(filename):
    f = open(filename, 'r')
    L = []
    for line in f:
        a, b = line.split()
        L.append([float(a), float(b)])
    f.close()
    print 'starting from file', filename
else:
    #L = [[0.25, 0.25], [0.25, 0.75], [0.75, 0.25], [0.75, 0.75]]
    delxy = sigma + ((1.0 - 2*N_sqrt*sigma) / (2*N_sqrt))
    two_delxy = 2 * delxy
    L = [[delxy + i * two_delxy, delxy + j * two_delxy] for i in range(N_sqrt) for j in range(N_sqrt)]

f = open(filename, 'w')
for a in L:
   f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
f.close()

print "eta: ", eta
print "psi: ", Psi_6(L, sigma)
# Run simulation
psi_6 = 0.0  # used to sum values of psi_6 for a particular eta
mean_psi_6 = [] # list to store absolute mean value for an eta
eta_for_psi_6 = [] # list to store eta
n_steps = 1000000
for steps in range(n_steps):
    # compute psi_6 every 100 steps
    if (steps % 100 == 0):
        psi_6 += Psi_6(L, sigma)
    # decrease eta every 10000 steps
    if (steps % 10000 == 0):
        mean_psi_6.append(abs(psi_6/float(100)))
        #mean_psi_6.insert(0, abs(psi_6/float(100))) 
        eta_for_psi_6.append(eta)
        #eta_for_psi_6.insert(0, eta)
        eta -= 0.02
        # terminagte simulation when eta < 0.2
        if eta < 0.2: break
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

# plot of the mean absolute value of Psi_6 as a function of density eta
pylab.xlabel('$eta$', fontsize=14)
pylab.ylabel('$Global Order Parameter$', fontsize=14)
pylab.title('Mean absolute value of Psi_6 as a function of density eta')
#mean_psi_6.reverse()
#eta_for_psi_6.reverse()
pylab.plot(eta_for_psi_6, mean_psi_6, 'bs')
pylab.savefig('Plot_Global_Order_Parameter.png')
pylab.show()






