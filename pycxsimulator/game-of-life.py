import matplotlib
matplotlib.use('TkAgg')
from pylab import *

L = 100 # Size of Array
p = 0.6  # Probability of panic
r = 1   # Radius of neighborhood

def initialize():
    global students, students_temp
    students = zeros([L, L])
    for x in range(L):
        for y in range(L):
            students[x, y] = 1 if random() < p else 0
    students_temp = zeros([L,L])

def observe():
    global students
    cla() # to clear the visualization space
    imshow(students, vmin = 0, vmax = 1) #imshow() is from MatLab

def update():
    global students, students_temp
    for x in range(L):
        for y in range(L):
            n = 0
            for dx in range(-r, r+1):
                for dy in range(-r, r+1):
                    if 0 <= x+dx < L and 0 <= y+dy < L:
                        n += students[x+dx, y+dy]
            if students[x, y] == 0:
                students_temp[x, y] = 1 if n == 3 else 0
            else:
                students_temp[x, y] = 1 if 2 <= n-1 <= 3 else 0


    students, students_temp = students_temp, students
    # this is better for memory management!

import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])
