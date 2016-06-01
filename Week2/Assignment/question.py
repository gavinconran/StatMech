#Program A3:
'''
import random

import random
for iter in range(1000000):
    position = (position + 1) % N

N = 20; position = 0
for iter in range(1000000):
    if random.uniform(0.0, 1.0)  < 0.4: 
        position = (position - 1) % N
        left += 1
    elif random.uniform(0.0, 1.0)  > 0.6:
        position = (position + 1) % N
        right+=1
    else:
        stay += 1


# program B3

import random
N = 20; position = 0
for iter in range(1000000):
    Upsilon = random.uniform(0.0, 1.0)
    if Upsilon < 0.4: 
        position = (position - 1) % N
        left += 1
    elif Upsilon  > 0.6:
        position = (position + 1) % N
        right+=1
    else:
        stay += 1

# program C3
import random

N = 20; position = 0
for iter in range(1000000):
    if random.uniform(0.0, 1.0) > 0.2: 
        if random.uniform(0.0, 1.0) < 0.5:
            position = (position + 1) % N
            right+=1
        stay += 1
    else: 
        position = (position - 1) % N
        left += 1
'''
# program D3
import random
stay=0
left=0
right=0
N = 20; position = 0
for iter in range(1000000):
    if random.uniform(0.0, 1.0) > 0.2: 
        if random.uniform(0.0, 1.0) < 0.5:
            position = (position + 1) % N
            right+=1
        if random.uniform(0.0, 1.0) > 0.5:
            position = (position - 1) % N
            left+=1
        stay+=1

print stay/float(1000000)
print left/float(1000000)
print right/float(1000000)

