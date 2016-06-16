# transforms a uniformly generated randomvariable (Upsilon) into
# an "x" position on the x-axis of the gaussian PDF 

import scipy.special, random, math, pylab

n_trials = 100000
data = []
for trial in xrange(n_trials):
    Upsilon = random.uniform(0.0, 1.0)
    # calculate x from the inverse error function
    x = math.sqrt(2.0) * scipy.special.erfinv(2.0 * Upsilon - 1.0)
    data.append(Upsilon)
    #print x


pylab.hist(data, bins=100, normed='True')
pylab.xlabel('$x$', fontsize=16)
pylab.ylabel('$\pi(x)$', fontsize=16)
#x = [a / 100.0 for a in xrange(1, 101)]
#y = [0.5 / math.sqrt(a) for a in x]
#pylab.plot(x, y, linewidth=1.5, color='r')
pylab.title('Theoretical distribution $\pi(x)$\
    \n histogram for '+str(len(data))+' samples',fontsize=16)
pylab.show()

