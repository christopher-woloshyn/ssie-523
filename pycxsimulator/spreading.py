import matplotlib
matplotlib.use('TkAgg')
from pylab import *

L = 100 # Size of Array
p = 0.4  # Probability of panic
r = 1   # Radius of neighborhood

def initialize():
    global students, students_temp
    students = zeros([L, L])
    for x in range(L):
        for y in range(L):
            students[x, y] = 1 if random() < p else 0
    students[int(random()*100), int(random()*100)] = 2 #This is 1 adopter of the product
    students_temp = zeros([L,L])

def observe():
    global students
    cla() # to clear the visualization space
    imshow(students, vmin = 0, vmax = 2) #imshow() is from MatLab

def update():
    global students, students_temp
    for x in range(L):
        for y in range(L):
            if students[x, y] in [0, 2]:
                students_temp[x, y] = students[x, y]
            else:
                n = 0
                for dx in range(-r, r+1):
                    for dy in range(-r, r+1):
                        if 0 <= x+dx < L and 0 <= y+dy < L:
                            n += 1 if students[x+dx, y+dy] == 2 else 0
                students_temp[x, y] = 2 if n > 0 else 1

    students, students_temp = students_temp, students
    # this is better for memory management!

import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])
