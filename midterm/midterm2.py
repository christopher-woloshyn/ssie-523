from pylab import *

def initialize():
    global x, y, yresult
    x = 0.1
    y = 0.1
    yresult = []

def observe():
    global x, y, yresult
    yresult.append(y)

def update(c):
    global x, y, yresult
    nx = x + x*(1 - x)
    ny = y - 0.5*y + c*x*y*(1 - y)
    x, y = nx, ny

def plot_asymptotic_states(c):
    initialize()
    for t in range(50): # first 50 steps are discarded
        update(c)
    for t in range(50): # second 50 steps are collected
        update(c)
        observe()
    plot([c] * 50, yresult, 'b.', alpha = 0.3)

def main():
    for c in arange(0, 3.5, 0.02):
        plot_asymptotic_states(c)

    xlabel('c')
    ylabel('y_eq')
    show()

main()
