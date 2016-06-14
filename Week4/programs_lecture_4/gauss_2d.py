# Python' random.gauss() uses same basic algo (Box-Muller) to
# generate standard iid random numbers

import random

nsamples = 100
for sample in range(nsamples):
    x, y = random.gauss(0.0, 1.0), random.gauss(0.0, 1.0)
    print x, y
