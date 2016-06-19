import random, math, pylab
#from matplotlib import pyplot
#from mpl_toolkits.mplot3d import Axes3D

x, y = 0.0, 0.0
delta = 0.1
n_trials = 40000000
n_hits = 0

x_pos = []
y_pos = []
z_pos = []

for i in range(n_trials):
    del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
    if math.sqrt((x + del_x)**2 + (y + del_y)**2) < 1.0:
        x, y = x + del_x, y + del_y
        z = random.uniform(-1.0,1.0)
    if x**2 + y**2 + z**2 < 1.0: 
        n_hits += 1
        #x_pos.append(x)
        #y_pos.append(y)
        #z_pos.append(z)
print n_hits / float(n_trials)

#fig = pylab.figure()
#ax = Axes3D(fig)
#ax.scatter(x_pos, y_pos, z_pos)
#pyplot.show()
