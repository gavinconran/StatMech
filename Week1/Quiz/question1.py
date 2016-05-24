# Program A1
import random
N = 20
position = 0
left = 0
right = 0
for t in range(100000):
    if random.uniform(0.0, 1.0) < 0.5:
        position = (position + 1) % N
        left += 1
    elif random.uniform(0.0, 1.0) > 0.5:
        position = (position - 1) % N
        right += 1

print left, right


# Program B1
import random
N = 20
position = 0
left = 0
right = 0
for t in range(100000):
    dir = random.choice([-1, 1])
    if (dir == -1): left += 1
    if (dir == 1): right += 1
    position = (position + dir) % N
print left, right

# Program B1
import random
N = 20
position = 0
left = 0
right = 0
for t in range(100000):
    if random.uniform(0.0, 1.0) < 0.5:
        position = (position + 1) % N
        left += 1
    else:
        position = (position - 1) % N
        right += 1
print left, right
