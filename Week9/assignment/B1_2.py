# B1.py

import random, math

def unit_sphere():
    x = [random.gauss(0.0, 1.0) for i in range(3)]
    norm =  math.sqrt(sum(xk ** 2 for xk in x))
    return [xk / norm for xk in x]

def minimum_distance(positions, N):
    dists = [math.sqrt(sum((positions[k][j] - positions[l][j]) ** 2 \
             for j in range(3))) for l in range(N) for k in range(l)]
    return min(dists)

def resize_disks(positions, r, N, gamma):
    Upsilon = minimum_distance(positions, N) / 2.0
    r = r + gamma * (Upsilon - r)
    return r

N = 15
# gamma is the annealing rate
gammas  = [0.0025] #0.05] #0.1] #0.0025] #0.5
#gammas = [0.0025, 0.1, 0.2]
min_density = 0.78

for gamma in gammas:
    print 'gamma', gamma
    for run in range(1): #  10):
        print 'run', run
        sigma  = 0.25
        r = 0.0
        positions = [unit_sphere() for j in range(N)]
        n_acc = 0
        step = 0
        while sigma > 1.e-8:
            step += 1
            if step % 500000 == 0:
                eta = N / 2.0 * (1.0 - math.sqrt(1.0 - r ** 2))
                print r, eta, sigma, acc_rate
            k = random.randint(0, N - 1)
            newpos = [positions[k][j] + random.gauss(0, sigma) for j in range(3)]
            norm = math.sqrt(sum(xk ** 2 for xk in newpos))
            newpos = [xk / norm for xk in newpos]
            new_min_dist = min([math.sqrt(sum((positions[l][j] - newpos[j]) ** 2 \
                       for j in range(3))) for l in range(k) + range(k + 1, N)])
            if new_min_dist > 2.0 * r:
                positions = positions[:k] + [newpos] + positions[k + 1:]
                n_acc += 1
            if step % 100 == 0:
                acc_rate = n_acc / float(100)
                n_acc = 0
                if acc_rate < 0.2:
                    sigma *= 0.5
                elif acc_rate > 0.8 and sigma < 0.5:
                    sigma *= 2.0
                r = resize_disks(positions, r, N, gamma)
                R = 1.0 / (1.0 / r - 1.0)
                eta = 1.0 * N / 2.0 * (1.0 - math.sqrt(1.0 - r ** 2))
        print 'final density: %f (gamma = %f)' % (eta, gamma)
        if eta > min_density:
            f = open('N_' + str(N) + '_final_'+ str(eta) + '.txt', 'w')
            for a in positions:
               f.write(str(a[0]) + ' ' + str(a[1]) + ' ' + str(a[2]) + '\n')
            f.close()


import pylab, numpy, mpl_toolkits.mplot3d

def draw_sphere(center, rad, col, ax, resolution):
    delta = numpy.pi / float(resolution)
    u, v = numpy.mgrid[0:2 * numpy.pi + delta:delta, 0:numpy.pi + delta * 0.5:delta * 0.5]
    x = center[0] + rad * numpy.cos(u) * numpy.sin(v)
    y = center[1] + rad * numpy.sin(u) * numpy.sin(v)
    z = center[2] + rad * numpy.cos(v)
    ax.plot_wireframe(x, y, z, color=col)

fig = pylab.figure()
ax = fig.gca(projection='3d')
ax.set_aspect('equal')
ax.set_axis_off()
draw_sphere([0.0, 0.0, 0.0], 1.0, 'r', ax, 40)
centers = [[(1.0 + R) * pos[j] for j in range(3)] for pos in positions]
for center in centers:
    draw_sphere(center, R, 'b', ax, 10)
ax.set_xlim(-1.0 - 2.0 * R, 1.0 + 2.0 * R)
ax.set_ylim(-1.0 - 2.0 * R, 1.0 + 2.0 * R)
ax.set_zlim(-1.0 - 2.0 * R, 1.0 + 2.0 * R)
pylab.show()
