import matplotlib
matplotlib.use('TkAgg')
from pylab import *

L = 100 # Size of Array
p = 0.5 # Probability of panic
r = 3 # Radius of neighborhood

def initialize():
    global students, students_temp
    students = zeros([L, L])
    for x in range(L):
        for y in range(L):
             #students[x, y] = 1 if random() < p else 0
            students[x, y] = 1 if y >  90 else 0
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
            size_of_nhood = 0
            for dx in range(-r, r+1):
                for dy in range(-r, r+1):
                    if not (x+dx >= L or x+dx < 0 or y + dy >= L or y+dy < 0):
                        size_of_nhood += 1
                        accum += students[(x+dx), (y+dy)]
            if accum/size_of_nhood == 0.5:
                students_temp[x, y] = students[x, y]
            students_temp[x, y] = round(accum/size_of_nhood) # Local Majority

    students, students_temp = students_temp, students
    # this is better for memory management!

import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])
