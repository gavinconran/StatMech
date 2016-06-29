# Applies Energy states in 3-D for multiple particles 

Emax = 50
States = []
count = 0
# 
for E_x in range(Emax):
    for E_y in range(Emax):
        for E_z in range(Emax):
            # restrict number of states < 5
            if E_x + E_y + E_z < 5:
                count += 1
                States.append(((E_x + E_y + E_z), (E_x, E_y, E_z)))
States.sort()
for k in range(count):
    print '%3d' % k, States[k][0], States[k][1]

#k = 0
#for state in States:
#    print '%3d' % k, state[0], state[1]
#    k += 1
