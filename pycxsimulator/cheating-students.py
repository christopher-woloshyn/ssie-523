import matplotlib
matplotlib.use('TkAgg')
from pylab import *

n = 1000

def initialize():
    global students
    students = [clip(normal(3.5, 0.5), 0, 4) for i in range(n)]

def observe():
    global students
    cla() # to clear the visualization space
    plot(students, '.')

def update():
    global students
    # THEORY - (students[i] will go up/down based on students[i-1])
    students2 = []
    for i in range(n):
        if i == 0:
            g = students[-1]
        else:
            g = students[i-1]
        students2.append((students[i] + g)/2)
    students = students2

import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])
