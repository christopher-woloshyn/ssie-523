from pylab import *

def main():
    L = 10
    g = 9.8

    xvalues, yvalues = meshgrid(arange(-10, 10 , 0.01), arange(-10, 10 , 0.01))

    xdot = yvalues
    ydot = -(g/L) * sin(xvalues)

    streamplot(xvalues, yvalues, xdot, ydot)

    show()

main()
