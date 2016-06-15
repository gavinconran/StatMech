m = 134456
n = 8121
k = 28411
idum = 1000
nu_set = set()
for iteration in xrange(200000):
    idum = (idum *  n + k) % m
    if (idum in nu_set): print "in"
    nu_set.add(idum)
    ran = idum / float(m)
    print idum, ran, iteration
