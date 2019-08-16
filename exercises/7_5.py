from pylab import *

def main():
    a = 1
    b = 2
    # equilibrium point should be at (b/a, 0)

    S, I = meshgrid(arange(0, 3, 0.1), arange(0, 3, 0.1))

    dS_dt = -a*S*I
    dI_dt = a*S*I - b*I

    streamplot(S, I, dS_dt, dI_dt)
    show()

main()
