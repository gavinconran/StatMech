# allows for direct sampling of a divergent distribution
# uses sample transformation from
# a uniform distribution to the divergent distribution x**gamma

import random, pylab,math

gamma = -0.5
data = []
n_trials = 10000
for trial in xrange(n_trials):
    x = (random.uniform(0.0, 1.0)) ** (1.0 / (gamma + 1.0))
    data.append(x)
    #print x


pylab.hist(data, bins=100, normed='True')
x = [a / 100.0 for a in xrange(1, 100)]
y = [1.0 / (2.0 * math.sqrt(a)) for a in x]
pylab.plot(x, y, 'red', linewidth = 2)
pylab.title('Theoretical distribution $\pi(x)={1}/{(2 \sqrt{x})}$ and normalized',fontsize=16)
pylab.xlabel('$x$', fontsize=18)
pylab.ylabel('$\pi(x)$', fontsize=18)
pylab.show()
