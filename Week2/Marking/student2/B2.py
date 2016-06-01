import random, pylab

def markov_sample(L,sigma,n_steps):
    sigma_sq = sigma ** 2
    delta = 0.1
    for steps in range(n_steps):
        a = random.choice(L) 
        b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
        min_dist = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in L if c != a) # square of minimum distance
        box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > 1.0 - sigma # check if collide in wall
        if not (box_cond or min_dist < 4.0 * sigma ** 2):
            a[:] = b
    return L

pos = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
n_steps = 1
N = 4
sigma = 0.1197
n_runs = 200000
histo_data = []
for run in range(n_runs):
    if run % 100000 == 0: print run
    pos = markov_sample(pos, sigma, n_steps)
    for k in range(N):
        histo_data.append(pos[k][0])
pylab.hist(histo_data, bins=100, normed=True)
pylab.xlabel('x')
pylab.ylabel('frequency')
pylab.title('Markov chain: x coordinate histogram (density eta=0.18)')
pylab.grid()
pylab.savefig('B2.png')
pylab.show()

