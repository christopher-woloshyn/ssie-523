from pylab import *

def main():
    a, b, c, d, K, J = 1, 1.5, 0.5, 1, 4, 0.65
    xvalues, yvalues = meshgrid(arange(0, 4, 0.01), arange(0, 4, 0.01))
    xdot = a * xvalues * (1 - (xvalues / K)) - b * (J * xvalues / (J + xvalues)) * yvalues
    ydot = -c * yvalues + d * (J * xvalues / (J + xvalues)) * yvalues
    streamplot(xvalues, yvalues, xdot, ydot)
    show()
#main()

# Later in lecture, uncovering chaos
# from period doubling bifurcations.

a = 4
def f(x):
    return a*x*(1-x)
x = 0.1
result = [x]
for t in range(100):
    x = f(x)
    result.append(x)
plot(result)
show()
