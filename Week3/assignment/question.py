# A5
import random, math, pylab
n_iter=100000
N = 20; position = 0
weight = [math.sin(k) + 1.5 for k in range(N)]
pos_list = [] 

"""
for iter in range(n_iter):
    dir = random.choice([-1, 1])
    new_position = (position + dir) % N
    if random.uniform(0.0, 1.0) < weight[new_position] / weight[position]:
        position = new_position
        pos_list.append(position)

# B5
for iter in range(n_iter):
    dir = random.choice([-1, 1])
    new_position = (position + dir) % N
    if random.uniform(0.0, 1.0) < weight[position] / weight[new_position]:
        position = new_position
    pos_list.append(position)

"""
# C5: The Correct Metropolis Algorithm
for iter in range(n_iter):
    dir = random.choice([-1, 1])
    new_position = (position + dir) % N
    if random.uniform(0.0, 1.0) < weight[new_position] / weight[position]:
        position = new_position
    pos_list.append(position)


"""
# A6

for iter in range(n_iter):
    Upsilon = random.uniform(0.0, 1.0)
    if Upsilon < 0.5: 
        new_position = (position + 1) % N
        if random.uniform(0.0, 1.0) < weight[new_position] / weight[position]: 
            position = new_position
        pos_list.append(position)



# B6
for iter in range(n_iter):
    Upsilon = random.uniform(0.0, 1.0)
    if Upsilon < 0.5: 
        new_position = (position + 1) % N
        if random.uniform(0.0, 1.0) < weight[position] / weight[new_position]: 
            position = new_position
    pos_list.append(position)


# C6
for iter in range(n_iter):
    Upsilon = random.uniform(0.0, 1.0)
    if Upsilon < 0.5: 
        new_position = (position + 1) % N
        if random.uniform(0.0, 1.0) < weight[new_position] / weight[position]: 
            position = new_position
    pos_list.append(position)
"""


pylab.plot(weight)
pylab.show()


