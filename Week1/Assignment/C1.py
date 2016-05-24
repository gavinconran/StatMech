import random, math
n_trials = 400000
n_hits = 0
var = 0.0

ObsMean = 0.0
ObsSqMean = 0.0
for iter in range(n_trials):
    x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
    
    Obs = 0.0
    ObsSq = 0.0
    if x**2 + y**2 < 1.0:
        n_hits += 1
        Obs = 4.0
        ObsSq = 16.0
    var += (Obs - math.pi)**2
    ObsMean += Obs
    ObsSqMean += ObsSq
print ObsSqMean/ float(n_trials)
print (ObsMean/ float(n_trials))**2
print 4.0 * n_hits / float(n_trials), math.sqrt(var / n_trials), math.sqrt((ObsSqMean/ float(n_trials)) \
                                                                  - (ObsMean / float(n_trials))**2) 
