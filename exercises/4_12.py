from pylab import *

# This is the function to model the prey's population.
def f(x, y, r, k, b):
    return x + (r*x*(1 - x/k)) - ((1 - 1/(b*y +1))*x)

# This is the function to model the predator's population.
def g(y, x, d, c):
    return y - (d*y) + (c*x*y)

# This is the main function to model the interaction
# between the predator and prey.
def main():
    # Prey data
    x = 7
    r = 1
    k = 5
    
    # Predator data
    y = 2
    d = 1
    
    # Other constants
    b = 1
    c = 1
    
    xresult = [x]
    yresult = [y]
    for t in range(100):
        nx = f(x, y, r, k, b)
        ny = g(y, x, d, c)
        x, y = nx, ny
        xresult.append(nx)
        yresult.append(ny)
    plot(xresult)
    plot(yresult)
        
main()