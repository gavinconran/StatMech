import random, math, pylab, cmath

def dist(x,y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return  math.sqrt(d_x**2 + d_y**2)
    
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

def delx_dely(x, y):
    d_x = (x[0] - y[0]) % 1.0
    if d_x > 0.5: d_x -= 1.0
    d_y = (x[1] - y[1]) % 1.0
    if d_y > 0.5: d_y -= 1.0
    return d_x, d_y

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

# The following lines of code differ from previous versions
# In the sense that it reconfigures the initial lattice structure
# 'Thermalizes' at eta = 0.72 and starts calculating Psi_6 with decrementing density

N = 64
N_sqrt = int(math.sqrt(N))
eta = 0.72
sigma_sq = (eta/N)/math.pi
sigma = math.sqrt(sigma_sq)
two_sigma = 2*sigma
delta = 0.5*sigma
delxy = 1.035*sigma #Values of delxy and two_delxy are determined by trials of plotting with n_steps = 0
two_delxy = 2*delxy

L = [[delxy + i * two_delxy, delxy + j * two_delxy] for i in range(N_sqrt) for j in range(N_sqrt)]
print 'Starting from a lattice configuration' #Start new configuration
filename = 'Disc_positions_64_track.txt'
f = open(filename, 'w')
for a in L:
    f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
f.close()
show_conf(L, sigma, 'Initial Configuration Markov Simulation, N=64, eta=0.72', 'Initial-plot.png')

ComPsi = []
DeltaRange = []
n_steps = 500000
for steps in range(n_steps): #'Thermalizing'
    a = random.choice(L)
    b = [(a[0] + random.uniform(-delta, delta))%1.0, (a[1] + random.uniform(-delta, delta))%1.0]
    fit = 1    
    for discpos in L:
        if discpos is not a:
            distval = dist(b,discpos)
            if distval < (2.0 * sigma):
                fit *= 0
            else:
                fit *= 1
    if fit is 1:
        a[:] = b
show_conf(L, sigma, 'Thermalized Configuration Markov Simulation, N=64, eta=0.72', 'Thermalized-plot.png')

#Now to begin computation of Psi_6 beginning from eta = 0.72
while eta >= 0.18:
    DeltaRange.append(eta)
    n_steps = 10000
    Psistep = 0j
    for steps in range(1,n_steps+1):
        a = random.choice(L)
        b = [(a[0] + random.uniform(-delta, delta))%1.0, (a[1] + random.uniform(-delta, delta))%1.0]
        fit = 1
        for discpos in L:
            if discpos is not a:
                distval = dist(b,discpos)
                if distval < (2.0*sigma):
                    fit *= 0
                else:
                    fit *= 1
        if fit is 1:
            a[:] = b
        if (steps%100 == 0):
            Psistep += abs(Psi_6(L,sigma))
            if steps == n_steps:
                ComPsi.append(Psistep/100.0)
    show_conf(L, sigma, '%s density, %s Disk, %s step Markov Simulation'%(eta,N,n_steps), '%s_Step-%s_Disk-plot.png'%(n_steps,N))
    eta -= 0.02
    sigma_sq = (eta/N)/math.pi
    sigma = math.sqrt(sigma_sq)
    delta = 0.5*sigma
    f = open(filename, 'w') #Update file
    for a in L:
        f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
    f.close()
    
DeltaRange.reverse()
ComPsi.reverse()
pylab.plot(DeltaRange, ComPsi, 'bs')
pylab.xlabel('Density')
pylab.ylabel('|Psi_6|')
pylab.title('Plot of mean |Psi_6| against system density (eta)')
pylab.grid()
pylab.savefig('Psi_6_decrement.png')
pylab.show()
