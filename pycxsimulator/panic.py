import matplotlib
matplotlib.use('TkAgg')
from pylab import *

L = 100 # Size of Array
p = 0.1 # Probability of panic

def initialize():
    global students, students_temp
    students = zeros([L, L])
    for i in range(L):
        for j in range(L):
            students[i, j] = 1 if random() < p else 0
    students_temp = zeros([L,L])

def observe():
    global students
    cla() # to clear the visualization space
    imshow(students, vmin = 0, vmax = 1) #imshow() is from MatLab

def update():
    global students, students_temp
    for x in range(L):
        for y in range(L):
            accum = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if (dx, dy) != (0, 0) and not (x+dx >= L or x+dx < 0 or y + dy >= L or y+dy < 0):

                        accum += students[(x+dx)%L, (y+dy)%L]
                        # MODULO opperation causes
                        # the boudaries to "wrap" around;
                        # i.e. x = 99 => x + dx = 100
                        # & 100 % L = 0 which is on the left
                        # side of the Matrix. Hence, this
                        # graduation ceremony takes place
                        # on a torus...

            if not students[x, y] and accum > 3:
                students_temp[x, y] = 1
            elif students[x, y] and accum < 3:
                students_temp[x, y] = 0
            else:
                students_temp[x, y] = students[x, y]
            if random() < 0.01:
                students_temp[x, y] = 1
            # 1% chance students becom panicky every timestep
    students, students_temp = students_temp, students
    # this is better for memory management!

#import pycxsimulator
#pycxsimulator.GUI().start(func=[initialize, observe, update])

pvalues = arange(0, 0.5, 0.05)
results = []
for p in pvalues:
    initialize()
    for t in range(100):
        update()
    results.append(mean(students))
plot(pvalues, results)
show()
