from pylab import *

def main():

    x, y = meshgrid(arange(-10, 10, 0.1), arange(-10, 10, 0.1))

    nx = y
    ny = x*y - x**2

    streamplot(x, y, nx, ny)
    show()

# This model has a saddle point at (0, 0)

main()
