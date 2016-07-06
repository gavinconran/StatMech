# canonic_harmonic_recursion_movie.py
# This recursion relation goes back to Landsberg in 1961.
# It relates the partition function of a system of N ideal bosons
# to the partition function of a single particle z
# and the partition functions Z of systems with fewer particles.
# So, we have arrived to an analytical solution


import math, pylab

# partitoon function of a single particle inside a 3-D harmonic trap
# ground state shifted so Energy levels = 1,...,k
def z(k, beta):
    return 1.0 / (1.0 - math.exp(- k * beta)) ** 3

def canonic_recursion(N, beta):
    Z = [1.0]
    for M in range(1, N + 1):
        Z.append(sum(Z[k] * z(M - k, beta) \
                     for k in range(M)) / M)
    return Z

N = 256
T_star = 0.6
beta = 1.0 / N ** (1.0 / 3.0) / T_star
Z = canonic_recursion(N, beta)
pi_k = [(z(k, beta) * Z[N - k] / Z[-1]) / float(N) for k in range(1, N + 1)]
# graphics output
pylab.plot(range(1, N + 1), pi_k, 'b-', lw=2.5)
pylab.ylim(0.0, 0.01)
pylab.xlabel('cycle length $k$', fontsize=16)
pylab.ylabel('cycle probability $\pi_k$', fontsize=16)
pylab.title('Cycle length distribution ($N=%i$, $T^*=%s$)' % (N, T_star), fontsize=16)
pylab.savefig('plot-prob_cycle_length.png')
