import random, math, pylab


# returns a Gaussian with unit standard deviation and zero mean, 
# restricted to the interval [-1.0, 1.0]
def gauss_cut():
    while True:
        x = random.gauss(0.0, 1.0)
        if abs(x) <= 1.0:
            return x

oneD_max = 0.5 / math.sqrt(2.0 * math.pi) # 2-D therefore 0.5 rather than 1.0 numerator
alpha = 0.5
nsteps = 1000000
samples_x = []
samples_y = []
x, y = 0.0, 0.0
for step in range(nsteps):
    xnew, ynew = gauss_cut(), gauss_cut()
    exp_new = - 0.5 * oneD_max * (xnew ** 2 + ynew ** 2) - alpha * (xnew ** 4 + ynew ** 4)
    exp_old = - 0.5 * oneD_max * (x ** 2 + y ** 2) - alpha * (x ** 4 + y ** 4)
    if random.uniform(0.0, 1.0) < math.exp(exp_new - exp_old):
        x = xnew
        y = ynew
    samples_x.append(x)
    samples_y.append(y)

pylab.hexbin(samples_x, samples_y, gridsize=50, bins=1000)
pylab.axis([-1.0, 1.0, -1.0, 1.0])
cb = pylab.colorbar()
pylab.xlabel('x')
pylab.ylabel('y')
pylab.title('A3_1')
pylab.savefig('plot_A3_1_GC.png')
pylab.show()
