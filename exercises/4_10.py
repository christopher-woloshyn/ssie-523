from pylab import *

# a is the growth rate of the population
def a(x, a0, k):
    return (((1. - a0)/k**2) * x * (x-k)) + 1

# f is the actual linear difference equation.
# It will look exponential
def f(x, a0, k):
    return a(x, a0, k)*x

# Main function because I like keeping my code organized.
def main():
    x  = 1.  # billions of humans
    a0 = 1.2 # initial growth rate of humans
    k  = 20  # Carrying capacity of Earth

    result = [x]
    for t in range(160): # t is in years
        x = f(x, a0, k)
        result.append(x)
    plot(result)

main()
