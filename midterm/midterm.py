from pylab import *

def initialize(i):
    global x, y, xresult, yresult, c
    x = 0.1
    y = 0.1
    xresult = [x]
    yresult = [y]
    c = i

def observe():
    global x, y, xresult, yresult
    xresult.append(x)
    yresult.append(y)

def update():
    global x, y, xresult, yresult, c
    nextx = x + x*(1 - x)
    nexty = y -0.5*y + c*x*y*(1 - y)
    x, y = nextx, nexty

def main():
    for c in arange(0, 2.1, 0.2):
        initialize(c)
        for t in range(30):
            update()
            observe()
        plot(yresult, 'r')
    plot(xresult, 'b')
    xlabel('Time (t)')
    ylabel('Population (x, y)')
    show()

main()
