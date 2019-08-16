from pylab import *

def initialize(x0, y0):
    global x, y, xresult, yresult
    x = x0
    y = y0
    xresult = [x]
    yresult = [y]
    
def observe():
    global x, y, xresult, yresult
    xresult.append(x)
    yresult.append(y)

def update():
    global x, y, xresult, yresult
    next_x = x + 0.1*(x - x*y)
    next_y = y + 0.1*(y - x*y)
    x, y = next_x, next_y
    
def main():
    for x0 in arange(0, 0.21, 0.03):
        for y0 in arange(0, 0.21, 0.03):
            initialize(x0, y0)
            for t in range(30):
                update()
                observe()
            plot(xresult, yresult, 'b')

main()