# extends to n dimensions
# puts points randomly with a uniform distribution
# on the surface of the hypersphere in n dimensions
# This algo places random peebles on the surface of a n-dimensional hypersphere

import random, math, pylab

dimensions = 5
nsamples = 20
for sample in xrange(nsamples):
    R = [random.gauss(0.0, 1.0) for d in xrange(dimensions)]
    # rescaling
    radius = math.sqrt(sum(x ** 2 for x in R))
    print [x / radius for x in R]

